from pandas_datareader import data as pdr
from yahoo_fin import stock_info as si
from pandas import ExcelWriter
import yfinance as yf
import pandas as pd
import requests
import datetime
import time

yf.pdr_override()

stocklist = si.tickers_sp500()
index_name = '^GSPC'  # S&P 500

final = []
index = []
n = -1

exportList = pd.DataFrame(columns=['Stock', "RS_Rating", "50 Day MA",
                                   "150 Day Ma", "200 Day MA", "52 Week Low", "52 week High"])
