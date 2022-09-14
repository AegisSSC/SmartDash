#THIS IS FOR THE STOCKS

# https://docs.data.nasdaq.com/




import quandl
import numpy as np
import pandas as pd



all_stocks = {'AAPL', 'GOOGL', 'TSLA', 'F', 'NVDA', 'VZ'}
start_dates = { 'AAPL' : "2010-01-01", 
                'GOOGL' : "2010-01-01", 
                'TSLA' : "2010-01-01", 
                'F' : "2010-01-01", 
                'NVDA' : "2010-01-01", 
                'VZ' : "2010-01-01"}
end_dates = { 'AAPL' : "2013-01-01", 
              'GOOGL' : "2013-01-01", 
              'TSLA' : "2013-01-01",
              'F' : "2013-01-01", 
              'NVDA' : "2013-01-01",
              'VZ' : "2013-01-01"}

def scrape_data(company, start, end):
    stock_data = quandl.get("WIKI/"+ company, start_date=start, end_date=end)
    stock_data.to_csv('stock_info/'+company+'.csv')



# read data in From csv
#  [ticker] | [number of shares] 


# query quandl for "Current" Prices



# Display current information


