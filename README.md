# Amazon Automated Product Purchase Script

Automate the process of purchasing products on Amazon using Selenium and Python.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

## Description

This script uses Selenium and Python to automate the process of purchasing multiple products from Amazon. It logs in using provided account credentials, navigates to product pages, and makes purchases for products that are in stock.

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Replace `/path/to/chromedriver` with the actual path to your ChromeDriver executable.
4. Update the `Product_list` with the URLs of the products you want to purchase.
5. Fill in the `login_dict` with your Amazon account credentials.
6. Run the script using `python automate_purchase.py`.

## Prerequisites

- Python 3.x
- ChromeDriver (Ensure you have the correct version for your Chrome browser)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/automated-amazon-purchase.git
