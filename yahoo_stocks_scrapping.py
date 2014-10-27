#!/usr/bin/python3

import requests
import csv
import pprint

stock_symbol = raw_input("Enter the stock symbol: ")
start_date = raw_input("Enter the start date in format MM-DD-YYYY: ")
end_date = raw_input("Enter the end date in format MM-DD-YYYY: ")

s_month, s_day, s_year = start_date.split('-')
e_month, e_day, e_year = end_date.split('-')

s_month = int(s_month) - 1
e_month = int(e_month) - 1

s_day = int(s_day) - 1

url='http://ichart.finance.yahoo.com/table.csv?s=%s&a=%d&b=%d&c=%d&d=%d&e=%d&f=%d' % (stock_symbol, int(s_month), int(s_day), int(s_year), int(e_month), int(e_day), int(e_year))

http_response=requests.get(url)
stock_reader=csv.reader(http_response.text.splitlines())
stock_data=list(stock_reader)
pprint.pprint(stock_data)

ds,open_,high,low,close,volume,adjc = stock_data[1]
print("The stock opened at {} on {}".format(open_,ds))
print("The average closing price was {0:.02f}".format(
    sum(float(item[4]) for item in stock_data[1:])/len(stock_data[1:])))