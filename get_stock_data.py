# Takes yahoo finance data in to a panda dataframe. Then converts it to csv file instead.

# ! to be used by "create_stat_libraries.py"

import yfinance as yf 

def get_stock_data(ticker, START, END):
    # ticker = 'AAPL'
    #     # ticker for desired company
    # START = "2015-01-01"
    #     # date to begin data collection
    # END = "2021-01-01"
        # date to stop data collection
    stock_prices = yf.download(ticker, START, END)
        # gets stock data from yahoo finance
        # yf.download(ticker, start date, end date)
    stock_prices = stock_prices[['Open','Close']]
        # lessens columns to just Date, Open, Close
    stock_prices.to_csv(ticker)
        # Converts panda dataframe to csv file

# test = get_stock_data('AAPL', "2015-01-01", "2021-01-01") 
