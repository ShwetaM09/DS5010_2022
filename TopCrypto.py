# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:43:25 2022

@author: amritanj
"""

import requests
from requests import Request, Session
import json
import pandas, csv



class topcrypto:
    
    def __init__(self):
       
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.headers = {'Accepts': 'application/json', 
                        'X-CMC_PRO_API_KEY': 'ecb1361b-a9fa-4536-8617-3fdffd549024' }
        self.session = Session()
        self.session.headers.update(self.headers)
        
    
    def topcoins(self, limit):
        
        url = self.url
        parameters = {'start': '1', 'limit': limit}
        r = self.session.get(url, params = parameters)
        self.data = r.json()['data']
        
        finalTable = []
        for temp in self.data:
            row = {}
            for temp2 in temp:
                if temp2 == "platform":
                    continue
                if temp2 == "quote":
                    temp3 = temp[temp2]['USD']
                    for temp4 in temp3:
                        row[temp4] = temp3[temp4]
                elif temp2 == "tags":
                    row[temp2] = (','.join(temp[temp2]))
                else :
                    row[temp2] = temp[temp2]
            finalTable.append(row)
            
        final = pandas.DataFrame(finalTable)
        final.index+=1
        final.to_csv('Top_Cryptocurrency_Data.csv')
        print("Requested file has been saved as 'Top_Cryptocurrency_Data.csv'")
       
        
o = topcrypto()

o.topcoins(10)
