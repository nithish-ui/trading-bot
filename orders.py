from logger import logger
import random

def place_market_order(client, symbol, side, quantity):
    try:
        logger.info(f"[MOCK] MARKET order: {symbol} {side} {quantity}")

        response = {
            "orderId": random.randint(10000, 99999),
            "status": "FILLED",
            "executedQty": str(quantity),
            "avgPrice": "65000"
        }

        logger.info(f"Response: {response}")
        return response

    except Exception as e:
        logger.error(f"Error placing MARKET order: {e}")
        raise


def place_limit_order(client, symbol, side, quantity, price):
    try:
        logger.info(f"[MOCK] LIMIT order: {symbol} {side} {quantity} @ {price}")

        response = {
            "orderId": random.randint(10000, 99999),
            "status": "NEW",
            "executedQty": "0",
            "avgPrice": "0"
        }

        logger.info(f"Response: {response}")
        return response

    except Exception as e:
        logger.error(f"Error placing LIMIT order: {e}")
        raise