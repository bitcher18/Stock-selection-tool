# 📈 Stock Selection Tool

This Python tool allows users to analyze historical closing prices of Malaysian stocks using the YFinance library.

## 🚀 Features

- **User Registration and Authentication**
- **Fetch Historical Closing Prices** for specified stock tickers.
- **Perform Analysis**:
  - Average Closing Price
  - Percentage Change (between first and last closing prices)
  - Highest and Lowest Closing Prices
- **Save and Retrieve Data** in CSV format.

## 🛠️ Setup and Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/bitcher18/Stock-selection-tool/edit/main/README.md
   cd stock-selection-tool
# Install Dependencies:

Ensure you have Python installed, then install the required libraries:
   ```bash
pip install pandas yfinance

# Run the Program
python main.py


# Project Structure
   ```bash
stock-selection-tool/
│-- main.py           # Handles user interactions
│-- functions.py      # Contains core functions (registration, authentication, data fetching, analysis)
│-- credentials.csv   # Stores user credentials (hashed passwords)
│-- user_data.csv     # Stores analysis results
│-- README.md         # Project documentation
└-- .gitignore        # Specifies files to exclude from version control



