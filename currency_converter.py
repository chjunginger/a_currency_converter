import pandas as pd
import urllib2
import json
__author__ = 'christianjunginger'

#Input variables
print('*'*40)
print('This is a currency converter for the most important currencies.\nPlease use ISO 4217 Currency codes (e.g. USD, EUR,...)')
print('*'*40)
homecurrency=raw_input("From which Currency? ").upper()
amount=raw_input("How many %s? "%homecurrency)
tocurrency=raw_input("To which Currency? ").upper()

# Getting the exchange rate
query='http://rate-exchange.appspot.com/currency?from=%s&to=%s'%(homecurrency.upper(),tocurrency.upper())
data  = json.load(urllib2.urlopen(query))


#Print out the exchange
print('*'*40)
print('%s %s are %s %s'%(amount, homecurrency,round(float(amount)*data['rate'],2),tocurrency))
print('*'*40)


##################
##
##
## This is how the output will look like (as of 3/16/15, 2:04pm GMT+1):
##
## wlan146-152:untitled christianjunginger$ python Currency-converter.py
## ****************************************
## This is a currency converter for the most important currencies.
## Please use ISO 4217 Currency codes (e.g. USD, EUR,...)
## ****************************************
## From which Currency? EUR
## How much EUR? 100
## To which Currency? USD
## ****************************************
## 100 EUR are 105.46 USD
## ****************************************



