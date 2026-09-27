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