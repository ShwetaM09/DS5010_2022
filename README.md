Title: Market Analysis of Data for Cryptocurrencies (MADC)

Authors:
Shagun Saboo, Amritanj Ayush, Parthasarathy Murugesan, Shweta Mishra

Summary: 

As the cryptocurrency market grows in popularity, so does the desire to monitor price trends to invest money wisely. Currently, the general public's knowledge and sources in this field are limited. We intend to bring the pricing trends and all the whereabouts of crypto to one place, making it accessible to developers working on related projects as well as normal-retail investors who just want to make better data-backed judgments when it comes to their investments.

With this idea in mind, we're developing a Python package that will collect data from all crypto currencies via API requests, then visualize and forecast price trends. We'll also use web scraping and natural language processing to extract pertinent news about the input currency. Following that, we will provide a final report with all of the above information.

Proposed Design:

The package aims to be a one-stop shop for cryptocurrency market statistics. The classes will be defined as below, underneath which sub-functions would be defined to implement to provide the package’s intended functionality.

•	class CryptoHistory:

This class offers methods for generating historical market data snapshots depending on the selected crypto currency and time range. The functions defined in this class include:
·	__init__() -> To verify the date and period instance
·	__str__() -> Format and return the historical data in String format
·	g_snap() ->  Provide historical snapshot of information regarding the price and volume distribution  of the specified cryptocurrency.

•	class CryptoCurrent: 

This class contains methods whose primary goal is to deliver the most up-to-date information for a given cryptocurrency on the global market. Functions include:

·	currentData() -> Provide  information regarding the latest price of the specified cryptocurrency  
·	global_info() -> Provide information regarding active cryptocurrencies, and dominance of top cryptocurrencies by Market Capitalization.

•	class TopCrypto: 

This class would give market capitalization-based pricing and volume information for the top cryptocurrencies on the global market. Functions would be defined as below:

·	Top10(), Top25(), Top100() -> Return volume capacity, latest price, and other metrics for Top 10, 25 & 100 Cryptocurrencies respectively.

•	class CryptoPredict:

This class would help us predict and visualize the price range for a particular time frame based on the trading pair that is mentioned (Restricted to popular pairs). 

·	PricePredict() ->  Return the price prediction for the specified Cryptocurrency and timeframe by using various models All these models would work with better efficiency and specified models based on micro factors for each of them.

•	class CryptoNews:

This class would allow us to visualize cryptocurrency prices and other metrics. Functions used:

·	CryptoVisualise() ->  Visualize the price and other metrics for cryptocurrencies.
·	CryptoLNews() -> Scrape and provide latest news from the crypto world.


External libraries that we will be requiring to accomplish aforementioned tasks include - requests, pandas, numpy, sklearn, matplotlib, statsmodels, yfinance, plotly, ipywidgets, tensorflow and pylab.

Anticipated Challenges:

More helper functions would be necessary than those listed above, as well as a comparison of different machine learning models to choose the most efficient model or the construction of an ensemble model. The APIs we intend to use must be reliable, otherwise we may be obliged to pay for a membership or look for alternatives in the future.

Website link:https://sabooshagun.github.io/madc/
For downloading the packages required use the following command: pip install -r requirements.txt



