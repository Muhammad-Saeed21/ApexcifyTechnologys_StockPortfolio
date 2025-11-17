# Project : Stock Portfolio Tracker
# Author : Muhammad Saeed
# Internship : Apexcify Technologys - Python Programming Internship
# Description : Simple Python program to calculate total stock investment using hardcoded prices.

# -----------------------------
# Hardcoded Stock Prices
# -----------------------------
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330
}


# -----------------------------
# Load Previous Saved Total
# -----------------------------
def load_previous_total():
    try:
        with open("portfolio.txt", "r") as file:
            data = file.read().strip()
            if data.isdigit():
                print(f"\n Previous total investment found: ${data}\n")
                return int(data)
        return 0
    except FileNotFoundError:
        print("\n No previous record found. Starting fresh.\n")
        return 0


# -----------------------------
# Process New Stock Inputs
# -----------------------------
def calculate_investment():
    total = load_previous_total()

    while True:
        stock = input(" Enter stock symbol (AAPL, TSLA, GOOGL, MSFT) or 'done' to finish: ").upper()

        if stock == "DONE":
            break

        if stock in stock_prices:
            try:
                qty = int(input(f" Enter quantity for {stock}: "))
                price = stock_prices[stock]
                investment = qty * price
                total += investment

                print(f" {stock}: {qty} × ${price} = ${investment}\n")

            except ValueError:
                print(" Invalid quantity! Please enter a number.\n")
        else:
            print(" Invalid stock name. Try again.\n")

    return total


# -----------------------------
# Save Final Total to File
# -----------------------------
def save_record(total):
    choice = input("\n Do you want to save this record? (Y/N): ").upper()

    if choice == "Y":
        with open("portfolio.txt", "w") as file:
            file.write(str(total))
        print(" Portfolio successfully saved in 'portfolio.txt'.")
    else:
        print(" Data not saved. Program ended without writing to file.")


# -----------------------------
# Main Program Execution
# -----------------------------
print("\n========== STOCK PORTFOLIO TRACKER ==========\n")

final_total = calculate_investment()
print(f"\n Total Investment Value: ${final_total}")

save_record(final_total)
