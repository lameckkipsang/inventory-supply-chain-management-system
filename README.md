# Inventory & Supply Chain Management System

A modular, command-line interface (CLI) application built in Python for managing inventory, tracking stock transactions, validating supplier credentials, and scraping live competitor market data with admin-authorized price synchronization.

This project emphasizes Object-Oriented Programming (OOP) principles, clean architecture, and local data persistence.

---

## Features

* **Interactive CLI Interface:** A continuous terminal menu for navigation across all system features.
* **Catalog Display & Portfolio Valuation:** Displays current inventory along with automatic calculation of total inventory portfolio value in KES.
* **Crash-Safe Stock Transactions:** Securely add or subtract stock quantities with input validation to prevent negative stock levels.
* **Dual-Tier Universal Web Scraper:** Lightweight competitor market scraper powered by `requests` and `BeautifulSoup4`. Uses domain configurations for targeted CSS scraping (e.g., Jumia, Kilimall) and automatically falls back to Schema.org JSON-LD metadata parsing for generic e-commerce platforms.
* **Admin-Authorized Price Synchronization:** Matches inventory products against scraped market data and updates catalog prices automatically behind password-protected authorization.
* **Data Validation & Persistence:** Regex-based email verification for supplier records, crash-proof numeric inputs, and relational CSV file persistence.

---

## Project Architecture & Separation of Concerns

The application is structured into modular components to ensure maintainability:

| Module | Responsibilities |
| :--- | :--- |
| `main.py` | Application entry point, interactive menu loop, user prompt dispatching |
| `models.py` | OOP domain models (`Product`, `Supplier` abstractions, property validation) |
| `system_manager.py` | Core business logic (portfolio valuation, stock updating, price sync) |
| `data_handler.py` | Reusable CSV read/write operations (`load_csv_data`, `save_csv_data`) |
| `market_scraper.py` | Dual-tier scraping engine, Schema.org JSON-LD parser, CLI data preview |
| `utilities.py` | Shared utilities (`get_valid_integer`, regex email checks, admin password verification) |

---

## Prerequisites & Setup

### 1. Requirements
* Python 3.8 or higher
* Required Python libraries: `requests`, `beautifulsoup4`

### 2. Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/lameckkipsang/inventory-supply-chain-management-system.git
cd inventory-supply-chain-management-system
pip install -r requirements.txt
```

### 3. Running the project
python main.py