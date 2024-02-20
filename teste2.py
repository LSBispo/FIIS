import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# Date must be in the fromat ("%Y-%m-%d") That is, year-month-day
start_date = '2019-1-1' #1 December 2020
end_date = '2024-2-2'    #2 February 2023
# "start_date" must be an older date than the "end_date"

stock = yf.download(tickers = "MXRF11.SA",
                  start = start_date,
                  end = end_date)

#print(amazon.head())



plt.figure(figsize=(14,5))
sns.set_style("ticks")
sns.lineplot(data=stock,x="Date",y='Close',color='firebrick')
sns.despine()
plt.title("The Stock Price",size='x-large',color='blue')





plt.show()