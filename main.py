from system_manager import display_product_catalog, process_stock_transaction

def main():
    """Main CLI entry point for the Inventory System."""
    while True:
        print("\nInventory & Supply Chain System")
        print("1. Display Product Catalog")
        print("2. Process Stock Transaction")
        print("3. Validate Supplier Email")
        print("4. Live Market Scraper")
        print("5. Exit")
        
        user_choice = input("\nSelect an option (1-5): ")
        
        if user_choice == '1':
            display_product_catalog()
            
        elif user_choice == '2':
            process_stock_transaction()