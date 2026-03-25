import click
from bot.orders import place_order
from bot.logging_config import setup_logging

setup_logging()

@click.command()
@click.option('--symbol', required=True)
@click.option('--side', required=True)
@click.option('--order_type', required=True)
@click.option('--quantity', type=float, required=True)
@click.option('--price', type=float, default=None)
def main(symbol, side, order_type, quantity, price):
    try:
        print("\n📌 Order Summary")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        print(f"Price: {price}")

        response = place_order(symbol, side, order_type, quantity, price)

        print("\n✅ Order Success")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")

    except Exception as e:
        print("\n❌ Order Failed")
        print(str(e))

if __name__ == "__main__":
    main()