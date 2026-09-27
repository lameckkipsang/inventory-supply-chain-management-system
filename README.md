# CLI Inventory & Supply Chain Management System

A modular, command-line interface (CLI) application built in Python for managing inventory, tracking stock transactions, and scraping live competitor market data. This project emphasizes Object-Oriented Programming (OOP) principles, clean architecture, and local data persistence.

## Features

* **Interactive CLI:** A continuous, user-friendly terminal menu for navigating system features.
* **Product Catalog & Valuation:** Displays current inventory with dynamic calculation of total portfolio value.
* **Stock Transactions:** Safe updating of stock quantities with crash-prevention and negative-stock validation.
* **Live Market Scraper:** Integrated web scraper utilizing `BeautifulSoup4` to pull live competitor pricing from Jumia, saving the output for offline analysis.
* **Data Persistence:** Relational CSV file management acting as a lightweight local database.
* **Data Validation:** Regex-powered email validation for supplier contacts and robust error handling for user inputs.

## Project Architecture (Separation of Concerns)

The application is heavily modularized to ensure maintainability:
* `main.py`: The core application loop and CLI interface.
* `models.py`: OOP definitions including the base `Product` class, encapsulation properties, and polymorphic `Supplier` subclasses.
* `system_manager.py`: Core business logic bridging user inputs and data files.
* `data_handler.py`: Safe read/write operations for CSV persistence.
* `market_scraper.py`: Web scraping logic with robust network error handling.
* `utilities.py`: Shared helper functions, including regex validation and crash-safe inputs.

## Prerequisites

To run this project, you will need Python 3.x installed on your machine along with the following external libraries:

```bash
pip install requests beautifulsoup4