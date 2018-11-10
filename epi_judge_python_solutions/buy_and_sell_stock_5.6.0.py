from test_framework import generic_test

def buy_and_sell_stock_once(prices):
    buy_price = float('inf')
    profit = 0

    for price in prices:
        profit = max(price-buy_price, profit)
        buy_price = min(buy_price, price)
    return profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
