import pandas as pd
import yfinance as yf

# 1. Function to register a new user
def register_user(email, password):
    try:
        # Create a DataFrame with the new user data
        new_user = pd.DataFrame([[email, password]], columns=["Email", "Password"])
        # Append to 'users.csv' (create it if it doesn't exist)
        new_user.to_csv("users.csv", mode='a', header=not pd.io.common.file_exists("users.csv"), index=False)
        return "Registration successful!"
    except Exception as e:
        return f"Error during registration: {e}"

# 2. Function to authenticate an existing user
def authenticate_user(email, password):
    try:
        # Read 'users.csv' into a DataFrame
        users = pd.read_csv("users.csv")
        # Check if the email and password match any row
        if ((users["Email"] == email) & (users["Password"] == password)).any():
            return True  # Successful login
        return False  # No match found
    except FileNotFoundError:
        return False  # If the file doesn't exist, return False

# 3. Function to fetch closing prices for a stock
def get_closing_prices(ticker, start_date, end_date):
    try:
        # Fetch stock data using yfinance
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        return stock_data['Close']
    except Exception as e:
        return f"Error fetching data: {e}"

# 4. Function to analyze closing prices
def analyze_closing_prices(data):
    if data.empty:
        return "No data available for analysis."
    
    # Perform basic analysis
    avg_price = data.mean()
    percentage_change = ((data.iloc[-1] - data.iloc[0]) / data.iloc[0]) * 100
    highest_price = data.max()
    lowest_price = data.min()

    return {
        "Average Price": avg_price,
        "Percentage Change": percentage_change,
        "Highest Price": highest_price,
        "Lowest Price": lowest_price
    }

# 5. Function to save analysis results to a CSV file
def save_to_csv(data, filename="user_data.csv"):
    try:
        # Convert the data dictionary to a DataFrame and append to CSV
        df = pd.DataFrame([data])
        df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)
        return "Data saved successfully!"
    except Exception as e:
        return f"Error saving data: {e}"

# 6. Function to read saved data from a CSV file
def read_from_csv(filename="user_data.csv"):
    try:
        # Read the CSV file into a DataFrame
        data = pd.read_csv(filename)
        return data
    except FileNotFoundError:
        return "No data found."

    
