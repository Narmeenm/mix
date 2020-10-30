import pandas as pd

from iexfinance.refdata import get_symbols
from iexfinance.stocks import Stock

api_key ="pk_8361f2e58b9d4895bb408c3628f36de3"

sy =get_symbols(output_format='pandas', token=api_key)

tsla = Stock('AAPL', token=api_key)
price = tsla.get_quote()
print(type(price))
book = tsla.get_book()
last = price['latestPrice']

print(last)

print(price)
