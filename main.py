import yfinance as yf
import pandas as pd
from funtion import register_user, authenticate_user, get_closing_prices, analyze_closing_prices, save_to_csv, read_from_csv

# File paths
USERS_FILE = "users.csv"
USER_DATA_FILE = "user_data.csv"

def display_main_menu():
    """Display the main menu options."""
    print("\nOptions:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def display_logged_in_menu():
    """Display the options available after login."""
    print("\nOptions:")
    print("1. Fetch and Analyze Stock")
    print("2. View Saved Data")
    print("3. Logout")

def get_user_credentials():
    """Prompt user for email and password and return them."""
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    return email, password

def handle_registration():
    """Handle user registration process."""
    email, password = get_user_credentials()
    if register_user(email, password, USERS_FILE):
        print("Registration successful!")
    else:
        print("Registration failed. Please try again.")

def handle_login():
    """Handle user login process and subsequent actions."""
    email, password = get_user_credentials()
    if authenticate_user(email, password, USERS_FILE):
        print("Login successful!")
        user_dashboard(email)
    else:
        print("Invalid email or password.")

def fetch_and_analyze_stock(email):
    """Fetch and analyze stock data based on user input."""
    ticker = input("Enter the stock ticker (e.g., 1155.KL): ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    try:
        closing_prices = get_closing_prices(ticker, start_date, end_date)
        if closing_prices.empty:
            print(f"Could not retrieve data for {ticker}. Please try again.")
            return

        analysis_results = analyze_closing_prices(closing_prices)

        # Display analysis results
        print("\nAnalysis Results:")
        for key, value in analysis_results.items():
            print(f"{key}: {value}")

        # Save data to CSV
        save_data = {
            "email": email,
            "ticker": ticker,
            "start_date": start_date,
            "end_date": end_date,
            "Average Closing Price": analysis_results["Average Closing Price"],
            "Percentage Change": analysis_results["Percentage Change"],
            "Highest Closing Price": analysis_results["Highest Closing Price"],
            "Lowest Closing Price": analysis_results["Lowest Closing Price"]
        }
        save_to_csv(save_data, USER_DATA_FILE)
        print("Data saved successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

def view_saved_data():
    """Display previously saved user data."""
    try:
        saved_data = read_from_csv(USER_DATA_FILE)
        if saved_data.empty:
            print("No data found.")
        else:
            print("\nPreviously Saved Data:")
            print(saved_data)
    except Exception as e:
        print(f"Error reading data: {e}")

def user_dashboard(email):
    """Provide logged-in users with options to fetch data, view saved data, or logout."""
    while True:
        display_logged_in_menu()
        choice = input("Please choose an option (1/2/3): ").strip()

        if choice == '1':
            fetch_and_analyze_stock(email)
        elif choice == '2':
            view_saved_data()
        elif choice == '3':
            print("Logging out.")
            break
        else:
            print("Invalid option. Please try again.")

def main():
    """Main function to run the Stock Selection Tool."""
    print("Welcome to the Stock Selection Tool!")

    while True:
        display_main_menu()
        choice = input("Please choose an option (1/2/3): ").strip()

        if choice == '1':
            handle_registration()
        elif choice == '2':
            handle_login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
