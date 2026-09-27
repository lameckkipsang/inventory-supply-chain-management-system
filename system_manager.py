from data_handler import load_csv_data, save_csv_data
from utilities import get_valid_integer

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