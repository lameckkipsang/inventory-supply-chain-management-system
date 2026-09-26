import csv
import requests
from bs4 import BeautifulSoup

def scrape_market_prices(target_url, output_csv_file):
    """Scrapes competitor pricing to generate market data for offline analysis."""
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        network_response = requests.get(target_url, headers=headers, timeout=10)
        network_response.raise_for_status()
        
        parsed_html = BeautifulSoup(network_response.text, "html.parser")
        product_elements = parsed_html.select(".prd _fb col c-prd")
        
        scraped_products = []
        for product in product_elements:
            title_element = product.select_one(".name")
            price_element = product.select_one(".prc")
            
            if title_element and price_element:
                scraped_products.append({
                    "Title": title_element.text.strip(),
                    "Category": "Smartphones",
                    "Price": price_element.text.strip(),
                    "Link": target_url
                })
        
        if len(scraped_products) > 0:
            csv_headers = ["Title", "Category", "Price", "Link"]
            with open(output_csv_file, mode="w", newline="", encoding="utf-8") as file_pointer:
                csv_writer = csv.DictWriter(file_pointer, fieldnames=csv_headers)
                csv_writer.writeheader()
                csv_writer.writerows(scraped_products)
            print(f"Scraped {len(scraped_products)} products into {output_csv_file}")
        else:
            print("No products found on the target page.")
            
    except requests.exceptions.RequestException as network_error:
        print(f"Failed to scrape data: {network_error}")