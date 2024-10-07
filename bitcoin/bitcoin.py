import requests
import sys


def main():
    # Check if the user provided a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <amount>")
        sys.exit(1)

    # Try to convert the argument to a float
    try:
        amount = float(sys.argv[1])
    except ValueError:
        print("Error: Amount must be a number.")
        sys.exit(1)

    # Make API request to get current Bitcoin price
    try:
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Convert the response to JSON
        # Extract the price as a float
        bitcoin_price = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        print("Error: Unable to retrieve Bitcoin price.")
        sys.exit(1)

    # Calculate the total cost in USD
    total_cost = amount * bitcoin_price

    # Print the cost formatted as a currency string
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
