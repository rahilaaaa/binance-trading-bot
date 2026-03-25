import os
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.client = Client(
            os.getenv("BINANCE_API_KEY"),
            os.getenv("BINANCE_SECRET_KEY")
        )
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, **kwargs):
        try:
            return self.client.futures_create_order(**kwargs)

        except BinanceAPIException as e:
            logging.error(f"Binance API Error: {e.message}")
            raise Exception(f"API Error: {e.message}")

        except BinanceRequestException as e:
            logging.error(f"Network Error: {str(e)}")
            raise Exception("Network error: unable to reach Binance")

        except Exception as e:
            logging.error(f"Unexpected Error: {str(e)}")
            raise