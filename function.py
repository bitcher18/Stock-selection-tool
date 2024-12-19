import yfinance as yf
import pandas as pd
import os
import csv
def register_user(email, password, users_file):
    # Check if users file exists and read it
    users = {}
    if os.path.exists(users_file):
        with open(users_file, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                users[row[0]] = row[1]
    
    # Register new user if not already registered
    if email not in users:
        users[email] = password
        with open(users_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([email, password])
        return True
    else:
        print("This email is already registered.")
        return False


def authenticate_user(email, password, users_file):
    """Authenticate a user based on stored credentials."""
    if os.path.exists(users_file):
        with open(users_file, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == email and row[1] == password:
                    return True
    return False

def get_closing_prices(ticker, start_date, end_date):
    """Fetch historical closing prices for the given stock ticker and period using YFinance."""
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        return stock_data['Close']
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.Series()

def analyze_closing_prices(data):
    """Perform basic analysis on the closing prices."""
    analysis = {
        "Average Closing Price": round(float(data.mean()), 2),
        "Percentage Change": round(float(((data.iloc[-1] - data.iloc[0]) / data.iloc[0]) * 100), 2),
        "Highest Closing Price": round(float(data.max()), 2),
        "Lowest Closing Price": round(float(data.min()), 2)
    }
    return analysis

def save_to_csv(data, filename):
    """Save user interactions to a CSV file."""
    file_exists = os.path.exists(filename)
    with open(filename, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        # Convert all values in data to strings to ensure compatibility
        writer.writerow({key: str(value) for key, value in data.items()})

def read_from_csv(filename):
    """Retrieve and display saved data from the CSV file."""
    if os.path.exists(filename):
        data = pd.read_csv(filename)
        return data
    else:
        print("No data found.")
        return pd.DataFrame()
