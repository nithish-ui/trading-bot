import argparse
from orders import place_market_order, place_limit_order

def validate_args(args):
    if args.side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if args.type not in ["MARKET", "LIMIT"]:
        raise ValueError("Type must be MARKET or LIMIT")

    if args.type == "LIMIT" and args.price is None:
        raise ValueError("Price is required for LIMIT orders")


def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_args(args)

        # Since we're mocking, no API client needed
        client = None

        print("\nOrder Summary:")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")

        if args.type == "MARKET":
            response = place_market_order(client, args.symbol, args.side, args.quantity)
        else:
            response = place_limit_order(client, args.symbol, args.side, args.quantity, args.price)

        print("\nResponse:")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

        print("\nSUCCESS")

    except Exception as e:
        print(f"\nFAILED: {e}")


if __name__ == "__main__":
    main()