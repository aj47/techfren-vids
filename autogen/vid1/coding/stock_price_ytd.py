# filename: stock_price_ytd.py

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package])

install('yfinance')
install('matplotlib')

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Define the ticker symbols: NVDA and TSLA
ticker_symbols = ["NVDA", "TSLA"]

# Initialize an empty dataframe
prices = pd.DataFrame()

# Fetch the data for each ticker
for symbol in ticker_symbols:
    data = yf.download(symbol, start='2022-01-01', end=pd.to_datetime('now').strftime('%Y-%m-%d'))['Close']
    prices = pd.concat([prices, data], axis=1)

# Set the column names to the ticker symbols
prices.columns = ticker_symbols

# Plot the data
prices.plot(figsize=(14, 7))

# Set title and labels
plt.title('NVDA and TSLA Stock Prices Year-To-Date (YTD)')
plt.xlabel('Date')
plt.ylabel('Price (in USD)')

# Show the plot
plt.show()