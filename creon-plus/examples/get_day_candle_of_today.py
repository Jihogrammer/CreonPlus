from utils.creon_historical_price import request_min_price_by_date


def example():
    result = request_min_price_by_date('A000660', 20220501, 20220510)
    for candle in result:
        print(result)
