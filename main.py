import sys
from system_manager import display_product_catalog, process_stock_transaction
from utilities import validate_email_address
from market_scraper import scrape_market_prices
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

        elif user_choice == '3':
            email_input = input("Enter supplier email to validate: ")
            is_valid = validate_email_address(email_input)
            if is_valid:
                print("Success: Email format is valid.")
            else:
                print("Error: Invalid email format.")
                
        elif user_choice == '4':
            target_url = input("Enter valid Jumia category URL to scrape: ")
            output_file = "live_market_data.csv" 
            print(f"Initializing scraper for {target_url}...")
            scrape_market_prices(target_url, output_file)
            
        elif user_choice == '5':
            print("Exiting Inventory System. Goodbye!")
            sys.exit()
            
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()