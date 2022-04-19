# -*- coding: utf-8 -*-
"""CryptoPredict.ipynb

Author : Parthasarathy

Original file is located at
    https://colab.research.google.com/drive/1rg1wFX8LEd9P90-Pff7ohesRVEBPCg-D
"""

import io
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files
import datetime
from statsmodels.tsa.statespace.sarimax import SARIMAX

class CryptoPredict:
  api_token = ""
  def __init__(self):
    self.api_token = "625ce48f84b4d3.50518364"
  
  def printing(self):
    return self.api_token

  def pricePredict(self,market_type,end_date):
    response=requests.get(f'https://eodhistoricaldata.com/api/eod/{market_type}.CC?api_token={self.api_token}&order=d&fmt=json')
    json_data=json.loads(response.content)
    df=pd.DataFrame(json_data)
    df_set=df.iloc[::-1].reset_index()
    df_set.drop(columns=['index'],inplace=True)
    df_set.set_index(['date'],inplace=True)
    df_set.fillna(0,inplace=True)
    model = SARIMAX(df_set["close"], trend='n', order=(0,1,0), seasonal_order=(1,1,1,12), freq="D")
    results_ARIMA = model.fit(disp=-1)
    start_date = df_set.last_valid_index()
    pred = results_ARIMA.predict(start=str(start_date), end=end_date, dynamic=True)
    return pred

  def visualizePredict(self,pred):
    plt.figure(figsize=(30,10))
    plt.plot(pred, label='prediction')
    plt.ylabel("Price")
    plt.xticks(rotation=90)
    plt.title("Seasonal ARIMA Prediction")
    plt.legend()
    plt.tight_layout()
    plt.show()
