# 📈 Stock Selection Tool

This Python tool allows users to analyze historical closing prices of Malaysian stocks using the YFinance library.



## **Features**
- **User Registration and Authentication**
- **Fetch Historical Closing Prices** for specified stock tickers.
- **Perform Analysis**:
  - Average Closing Price
  - Percentage Change (between first and last closing prices)
  - Highest and Lowest Closing Prices
- **Save and Retrieve Data** in CSV format.

---

## **Setup and Installation**

### **1. Install Python**
1. Download and install **Python 3.8 or later** from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. During installation, ensure you check the box for **"Add Python to PATH"**.

### **2. Install Visual Studio Code**
1. Download and install **Visual Studio Code** from [https://code.visualstudio.com/](https://code.visualstudio.com/).

### **3. Clone the Repository**
1. Open a terminal or command prompt.
2. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/bitcher18/Stock-selection-tool/edit/main/README.md

## **Environment Setup**
1.  Open a terminal in the project directory.
2.  Install Dependencies:
     ```bash
        pip install pandas yfinance



## **Project Structure**
The project consists of the following files:
 ```bash
    .
stock-selection-tool/
│-- main.py           # Handles user interactions
│-- functions.py      # Contains core functions (registration, authentication, data fetching, analysis)
│-- credentials.csv   # Stores user credentials (hashed passwords)
│-- user_data.csv     # Stores analysis results
│-- README.md         # Project documentation
└-- .gitignore        # Specifies files to exclude from version control
