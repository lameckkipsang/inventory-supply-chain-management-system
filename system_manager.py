from data_handler import load_csv_data, save_csv_data
from utilities import get_valid_integer

def display_product_catalog():
    """Loads and displays all products from the core database."""
    products_database_path = "products.csv"
    products = load_csv_data(products_database_path)
    
    if not products:
        print("No products found in the catalog.")
        return

    print("\nCurrent Inventory Catalog")
    for item in products:
        print(f"ID: {item['product_id']} | Name: {item['product_name']} | Stock: {item['stock_quantity']} | Price: KES {item['retail_price']}")