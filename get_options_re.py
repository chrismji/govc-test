# regex prototype to grab all necessary options data from just CUSIP

import yfinance as yf
from dateutil.parser import parse
import re

option_re = re.compile(
    r"^(?P<ticker>.+?)"
    r"(?P<date>\d{6})"
    r"(?P<type>[CP])"
    r"(?P<strike>\d+(?:\.\d+)?)$"
)
# [6 straight numbers --> date] [C or P = type] [rest = numbers] [everything before = ticker]

def get_options(CUSIP: str):
    items = re.match(option_re, CUSIP).groupdict()

    print(items)

    date = parse(items['date'], yearfirst=True)
    date = (date.strftime('%Y-%m-%d')) # smart read for date

    stock = yf.Ticker(items['ticker'])
    chain = stock.option_chain(date)
    if items['type'] == 'C':
        data = chain.calls
    elif items['type'] == 'P':
        data = chain.put
        
    return data[data['strike'] == int(items['strike'])]

print(get_options('RVMD260918C160'))