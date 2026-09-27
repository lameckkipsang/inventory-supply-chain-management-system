import csv
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

SITE_CONFIGS = {
    "jumia.co.ke": {
        "container": "article.prd",
        "title": ".name",
        "price": ".prc"
    },
    "kilimall.co.ke": {
        "container": ".product-item",
        "title": ".product-title",
        "price": ".product-price"
    }
}

def extract_via_selectors(soup, config, target_url):
    """Extracts products using site-specific CSS selectors."""
    products = []
    for element in soup.select(config["container"]):
        title_tag = element.select_one(config["title"])
        price_tag = element.select_one(config["price"])
        if title_tag and price_tag:
            products.append({
                "Title": title_tag.text.strip(),
                "Category": "General",
                "Price": price_tag.text.strip(),
                "Link": target_url
            })
    return products

def extract_via_schema_json(soup, target_url):
    """Extracts product data from standard Schema.org JSON-LD tags using type() and try/except."""
    products = []
    scripts = soup.find_all("script", type="application/ld+json")
    
    for script in scripts:
        if not script.string:
            continue
        try:
            data = json.loads(script.string)
            items = data if type(data) == list else [data]
            
            for item in items:
                try:
                    if type(item) == dict and item.get("@type") in ["Product", "IndividualProduct"]:
                        title = item.get("name")
                        offers = item.get("offers", {})
                        
                        price = None
                        currency = "KES"
                        
                        try:
                            if type(offers) == dict:
                                price = offers.get("price")
                                currency = offers.get("priceCurrency", "KES")
                            elif type(offers) == list and len(offers) > 0:
                                price = offers[0].get("price")
                                currency = offers[0].get("priceCurrency", "KES")
                        except (AttributeError, KeyError, IndexError):
                            pass
                            
                        if title and price:
                            products.append({
                                "Title": str(title).strip(),
                                "Category": "General",
                                "Price": f"{currency} {price}",
                                "Link": target_url
                            })
                except (AttributeError, KeyError, TypeError):
                    continue
                    
        except (json.JSONDecodeError, TypeError, AttributeError):
            continue
            
    return products

def scrape_market_prices(target_url, output_csv_file):
    """Scrapes market prices using site configs with Schema.org fallback."""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        response = requests.get(target_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        domain = urlparse(target_url).netloc.replace("www.", "")
        
        scraped_products = []
        
        if domain in SITE_CONFIGS:
            scraped_products = extract_via_selectors(soup, SITE_CONFIGS[domain], target_url)
        
        # Generic Schema.org fallback
        if not scraped_products:
            print("No domain match found. Attempting generic Schema.org extraction...")
            scraped_products = extract_via_schema_json(soup, target_url)
        
        if len(scraped_products) > 0:
            csv_headers = ["Title", "Category", "Price", "Link"]
            with open(output_csv_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=csv_headers)
                writer.writeheader()
                writer.writerows(scraped_products)
                
            print(f"\nSuccess: Scraped {len(scraped_products)} products into {output_csv_file}")
            print("Market Data Preview (First 5 Items)")
            for product in scraped_products[:5]:
                print(f"- {product['Title'][:35]}... | {product['Price']}")
        else:
            print("No products found on the target page.")
            
    except requests.exceptions.RequestException as network_error:
        print(f"Failed to scrape data: {network_error}")