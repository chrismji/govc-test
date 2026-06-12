import yfinance as yf
from dateutil.parser import parse

def get_options(ticker, type, date, strike):
    date = parse(date)
    date = (date.strftime('%Y-%m-%d')) # smart read for date
# option's tickers all seem to be [ticker][YYMMDD][C/P][strike], might be useful to read it that way
    stock = yf.Ticker(ticker)
    chain = stock.option_chain(date)
    if type == 'call':
        data = chain.calls
    elif type == 'put':
        data = chain.put
    
    return data[data['strike'] == strike]

print(get_options('RVMD', 'call', 'SEP 18 2026', 160)['lastPrice']) # example