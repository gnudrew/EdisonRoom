import yfinance as yf
import pyfolio as pf
fb = yf.Ticker('JHMT')
history = fb.history('max')
history.index = history.index.tz_localize('utc')
print(history.info())

returns = history.Close.pct_change()
print(returns)

pf.create_returns_tear_sheet(returns, live_start_date='2020-1-1')