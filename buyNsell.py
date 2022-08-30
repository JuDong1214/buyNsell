## Imports
import numpy as np
import pandas as pd
import yfinance as yf #Data Source
import plotly.graph_objs as go #Data Visualization
import csv
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc #might not be used
import matplotlib as mpl #might not be used
from matplotlib import dates, ticker #might not be used
import time 

def get_data():
    data = yf.download(tickers='ETH-USD', period = '10h', interval = '1m') #Ethereum, interval of 1 minute because we like dat
    return data

def create_graph(data, smallAvgRange, longAvgRange):
    df = pd.DataFrame(data) #Create Main Dataframe of data
   
    df['MAShort'] = df.Close.rolling(smallAvgRange).mean()
    df['MALong'] = df.Close.rolling(longAvgRange).mean()
   
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                        open=df.Open,
                                        high=df.High,
                                        low=df.Low,
                                        close=df.Close),
                          go.Scatter(x=df.index, y=df.MAShort, line=dict(color='black', width=1)),
                          go.Scatter(x=df.index, y=df.MALong, line=dict(color='blue', width=1))])
        # Add titles
    fig.update_layout(
        title='Etherium live share price evolution',
        yaxis_title='Etherium Price (US Dollars)')

    # X-Axes
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=6, label="6h", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    return df, fig

def buy_sell(shortAverage, longAverage, i, buySellToggle):
    if (shortAverage[i] > longAverage[i]) & (buySellToggle == 0):
        buySellToggle = 1
        return 'BUY HOLY SHIT MF BUY THAT SHIT DUMMY', buySellToggle
    if (shortAverage[i] < longAverage[i]) & (buySellToggle == 1):
        buySellToggle = 0
        return 'SELL OR ELSE U LOSE ALL UR MONEY O FUCK', buySellToggle
    else:
        return 'HOLD', buySellToggle
   


def main():
   

    smallAvgRange = 1
    longAvgRange = 10
    buySellToggle = 1
   
   
   
   
    while True:
        data = get_data()
        #print(data) #test
        df, fig = create_graph(data, smallAvgRange, longAvgRange)
        fig.show()
        #print(df) #test
        decision, buySellToggle = buy_sell(df.MAShort, df.MALong, len(df) - 1, buySellToggle)
        print(decision)
       
       
       
        time.sleep(30)

   

main()
