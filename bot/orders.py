import logging
from bot.client import BinanceClient
from bot.validators import *

client = BinanceClient()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        # Validation

        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)


        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logging.info(f"Order Request: {params}")

        response = client.place_order(**params)

        logging.info(f"Order Response: {response}")

        return response

    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        raise