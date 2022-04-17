# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:21:44 2022

@author: Shweta - 5110 - Project - Day 1
"""
from datetime import datetime
import time, requests, pandas, lxml
from lxml import html

class CryptoHistory:
    
    def format_date(date_datetime):
        date_timetuple = date_datetime.timetuple()
        date_mktime = time.mktime(date_timetuple)
        date_int = int(date_mktime)
        date_str = str(date_int)
        return date_str
    
    def subdomain(symbol, start, end, filter='history'):
         subdoma="/quote/{0}/history?period1={1}&period2={2}&interval=1d&filter={3}&frequency=1d"
         subdomain = subdoma.format(symbol, start, end, filter)
         return subdomain

    def header_function(subdomain):
        hdrs =  {"authority": "finance.yahoo.com",
                  "method": "GET",
                  "path": subdomain, #path key assigned as subdomain
                  "scheme": "https",
                  "accept": "text/html",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "en-US,en;q=0.9",
                  "cache-control": "no-cache",
                  "cookie": "Cookie:identifier",
                  "dnt": "1",
                  "pragma": "no-cache",
                  "sec-fetch-mode": "navigate",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-user": "?1",
                  "upgrade-insecure-requests": "1",
                  "user-agent": "Chrome/5.0 (Windows NT 11.0; Win64)"}
        return hdrs
    
    def scrape_page(url, header):
        pan = requests.get(url,headers=header)
        element_html = html.fromstring(pan.content)
        table = element_html.xpath('//table')
        table_tree = lxml.etree.tostring(table[0], method='xml')
        panda = pandas.read_html(table_tree)
        return panda
         
if __name__ == "__main__": 
    my_string = str(input('Enter start date(yyyy-mm-dd hh:mm): ')) #2022-04-14 18:22
    dt_start = datetime.strptime(my_string, "%Y-%m-%d %H:%M")
    my_string1 = str(input('Enter end date(yyyy-mm-dd hh:mm): ')) #2022-04-15 18:22
    dt_end=datetime.strptime(my_string1, "%Y-%m-%d %H:%M")
    start=CryptoHistory.format_date(dt_start)
    end=CryptoHistory.format_date(dt_end)
    symbol = input("Enter the cryptocurrency symbol (i.e,'CRYPTO_NAME'-USD): ") #BTC-USD
    r=CryptoHistory.subdomain(symbol, start, end)
    head=CryptoHistory.header_function(r)
    base_url = 'https://finance.yahoo.com'
    url = base_url + r
    data=CryptoHistory.scrape_page(url,head)
    data[0].to_csv('Requested_CryptoPr.csv')
    

    



