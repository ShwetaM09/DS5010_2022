# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 12:05:42 2022

@author: HP
"""
from dateutil.relativedelta import relativedelta
from datetime import datetime
import requests, pandas


class Cryptocurrent:
    
    def CryptoDate():
        end_date = datetime.today()
        st_date = end_date - relativedelta(seconds = 60)
        return st_date,end_date
    
    def EndUrl(symbol, st_date, end_date):
         EndU='/v2/price/values/'+ symbol +'?start_date=' + st_date.strftime("%Y-%m-%dT%H:%M") + '&end_date=' + end_date.strftime("%Y-%m-%dT%H:%M") +'&ohlc=true'
         base_url = 'https://production.api.coindesk.com'
         url = base_url + EndU
         return EndU , url
        
    def CryptoData(url,end_date):
        df = pandas.DataFrame(index=[0])
        temp_data_json = requests.get(url)
        temp_data = temp_data_json.json()
        df = pandas.DataFrame(temp_data['data']['entries'])
        df.columns = ['Timestamp', 'Open', 'High', 'Low', 'Close']
        df = df.drop(['Timestamp'], axis=1)
        df['Datetime'] = [end_date - relativedelta(minutes=len(df)-i) for i in range(0, len(df))]
        return df
        
    def CryptoMain(st_date,end_date):
        coindesk30_list =['BTC', 'ETH','XRP','LUNA','SOL','ADA', 'USDT', 'SHIB','DOGE', 'XLM', 'DOT', 'UNI', 'LINK', 'USDC', 'BCH', 'LTC', 'GRT', 'ETC', 'FIL', 'AAVE', 'ALGO','AVAX','ATOM','EOS','MATIC','MANA','ALGO','DOT','ICP','UST']
        raw_df = pandas.DataFrame()
        coin_df = pandas.DataFrame()
        l = pandas.DataFrame() 
        for coin in coindesk30_list:  
            x,y=Cryptocurrent.EndUrl(coin,st_date,end_date)
            l=Cryptocurrent.CryptoData(y,end_date)
            l['Symbol'] = coin
            print(coin)
            coin_df=l.append(coin_df)
            coin_df = coin_df.append(l)
        raw_df = raw_df.append(coin_df)
        raw_df = raw_df[['Datetime','Symbol','Open', 'High', 'Low', 'Close']].reset_index(drop=True)
        raw_df.sort_values(by=['Open'], inplace=True, ascending=False)
        raw_df.to_csv('CurrentCryptoPrice.csv', index=False) 
        
if __name__ == "__main__":
    st_date,end_date=Cryptocurrent.CryptoDate()
    Cryptocurrent.CryptoMain(st_date,end_date)
        
        
                
                
        
                
            
         
    
    
        
    