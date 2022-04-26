# -*- coding: utf-8 -*-
class Crypto_News:
  
  

  def crypto_news(self,crypto_name):
    """
    Description: This function allows you to fetch news related to crypto currency.
    You can fetch the entire bag of crypto news and can also fetch news specific to
    a coin.
    Parameters: Symbol of Crypto Currency
    Returns: News related to the parameter passed

    """

    return yf.Ticker(crypto_name).news
 

  def crypto_news_df(self,crypto_name):
    """
    Description: This function converts the list of dictionary to a data frame
    Parameters: Symbol of Crypto Currency
    Returns: News in a data-frame format
    """
    dfItem = pd.DataFrame.from_records(self.crypto_news(crypto_name))
    dfItem.drop(['uuid', 'publisher','providerPublishTime','type'], axis = 1)

    return dfItem

