# Capstone Project 1 — E-Commerce Web Automation Using Selenium WebDriver

## Project Overview

This project automates an e-commerce shopping workflow using **Python, Selenium WebDriver, and PyTest**.

The automation is implemented using the **Page Object Model (POM)** to keep page locators and test logic organized and maintainable.

The selected application for this capstone is:

**TutorialsNinja Demo**

Application URL:

https://tutorialsninja.com/demo/

---

## Objective

The objective of this project is to automate a customer purchasing workflow on an e-commerce website.

The automated workflow includes:

1. Launch the web application.
2. Load test data from a JSON file.
3. Log in using registered user credentials.
4. Search for a product.
5. Add the product to the shopping cart.
6. Open the shopping cart.
7. Update the product quantity.
8. Verify the product and cart details.
9. Validate the success alert.
10. Capture screenshots as execution evidence.
11. Generate an HTML execution report.

---

## Technologies Used

- Python 3.13
- Selenium WebDriver 4.49.0
- PyTest 9.1.1
- pytest-html 4.2.0
- Chrome WebDriver
- JSON
- Page Object Model (POM)

---

## Project Structure

```text
02_Capstone_Project/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── product_page.py
│   └── cart_page.py
│
├── tests/
│   ├── __init__.py
│   └── test_ecommerce.py
│
├── utils/
│   ├── __init__.py
│   ├── driver_factory.py
│   ├── test_data_reader.py
│   └── screenshot_helper.py
│
├── test_data/
│   └── test_data.json
│
├── screenshots/
│
├── reports/
│   └── execution_report.html
│
├── Videos/
│   └── README.md
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md