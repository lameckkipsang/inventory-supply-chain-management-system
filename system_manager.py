from data_handler import load_csv_data, save_csv_data
from utilities import get_valid_integer, verify_admin_authorization

def display_product_catalog():
    """Loads and displays all products, calculating total inventory valuation."""
    products_database_path = "products.csv"
    products = load_csv_data(products_database_path)
    
    if not products:
        print("No products found in the catalog.")
        return

    print("\nCurrent Inventory Catalog")
    total_portfolio_value = 0.0
    
    for item in products:
        stock = int(item['stock_quantity'])
        price = float(item['retail_price'])
        item_value = stock * price
        total_portfolio_value += item_value
        
        print(f"ID: {item['product_id']} | Name: {item['product_name'][:20]} | Stock: {stock} | Price: KES {price}")
        
    print("-" * 35)
    print(f"Total Inventory Value: KES {total_portfolio_value:,.2f}")

def process_stock_transaction():
    """Updates product stock and saves the changes to the CSV."""
    products_database_path = "products.csv"
    products = load_csv_data(products_database_path)
    
    target_id = input("Enter Product ID to update: ")
    # We are reuusing get_valid_integer function from utilities through the import
    quantity_change = get_valid_integer("Enter quantity to add (or negative to deduct): ")
    
    product_found = False
    for item in products:
        if item['product_id'] == target_id:
            current_stock = int(item['stock_quantity'])
            new_stock = current_stock + quantity_change
            
            if new_stock < 0:
                print("Error: Transaction would result in negative stock.")
                return
                
            item['stock_quantity'] = str(new_stock)
            product_found = True
            print(f"Success: {item['product_name']} stock updated to {new_stock}.")
            break
            
    if product_found:
        save_csv_data(products_database_path, products)
    else:
        print("Error: Product ID not found in database.")

def sync_prices_from_scraped_data():
    """Updates catalog product prices using scraped market data after admin authorization."""
    print("\n--- SENSITIVE OPERATION: Market Price Synchronization ---")
    
    # 1. Authorization check
    if not verify_admin_authorization():
        print("Error: Authorization failed. Price replacement cancelled.")
        return

    products_path = "products.csv"
    scraped_path = "live_market_data.csv"

    products = load_csv_data(products_path)
    scraped_data = load_csv_data(scraped_path)

    if not products or not scraped_data:
        print("Error: Missing catalog or scraped market data. Scrape data first (Option 4).")
        return

    updated_count = 0
    for product in products:
        prod_name_lower = product['product_name'].lower()
        
        for item in scraped_data:
            scraped_title_lower = item['Title'].lower()
            
            # Match product if catalog name appears in scraped title or vice versa
            if prod_name_lower in scraped_title_lower or scraped_title_lower in prod_name_lower:
                # Strip currency text and commas to isolate numeric price (e.g. "KES 15,000" -> "15000")
                raw_price = item['Price']
                clean_price_str = "".join(char for char in raw_price if char.isdigit() or char == '.')
                
                if clean_price_str:
                    old_price = product['retail_price']
                    product['retail_price'] = str(float(clean_price_str))
                    updated_count += 1
                    print(f"Updated '{product['product_name']}': KES {old_price} -> KES {product['retail_price']}")
                    break

    if updated_count > 0:
        save_csv_data(products_path, products)
        print(f"\nSuccess: Replaced prices for {updated_count} product(s) in {products_path}.")
    else:
        print("\nNo matching product titles found between inventory and scraped market data.")