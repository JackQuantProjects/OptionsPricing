import yfinance as yf
import numpy as np
import pandas as pd
from NewtonRaphson.NewtonRaphson import NewtonRaphson
from datetime import datetime
import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

#minimum time till expiration to avoid extremely small vegas
MIN_T = 7

symbol = "AMZN"
ticker = yf.Ticker(symbol)

def spotPrice(): # underlying price
    price = ticker.history(period="1d")["Close"].iloc[-1]
    return price

spot = spotPrice()

x = []  # maturity
y = []  # strike
z = []  # IV

def timeTillExpiration(date):

    expiry_date = datetime.strptime(date, "%Y-%m-%d")

    today = datetime.now()
    
    return (expiry_date - today).total_seconds() / (365 * 24 * 60 * 60)

def filterCalls(calls):
    '''
    removes the strikes less than 70% of the spot and more than 130% of the spot
    '''

    lower = 0.9 * spot
    upper = 1.1 * spot

    filtered_calls = calls[
        (calls["strike"] >= lower) &
        (calls["strike"] <= upper)
    ]
    return filtered_calls

def calcVolatility(call, T):
    S = spot
    K = call["strike"]
    r = 0.04
    Cm = (call["bid"] + call["ask"]) / 2
    '''
    print(
        "S", S, 
        "K:", K,
        "T:", T,
        "Bid:", call["bid"],
        "Ask:", call["ask"],
        "Cm:", Cm
    )
    '''

    return NewtonRaphson(S, K, T, r, Cm)

def build(call, expiry, T):

    K = call["strike"] # y
    IV = calcVolatility(call, T) # z
    x.append(T)
    y.append(K)
    z.append(IV)

    return "Successfully built data point"


def expiries():
    expiries = ticker.options
    return expiries

def expiriesIteration(expiries):
    for expiry in expiries:

        T = timeTillExpiration(expiry)
        
        if T < MIN_T / 365:
            continue

        #get the options with the current expiry
        chain = ticker.option_chain(expiry)

        calls = filterCalls(chain.calls)

        for index, call in calls.iterrows():
            try:
                build(call, expiry, T)
            except ValueError:
                print("vega most likely zero continuing")
                continue

def buildSurface():
    expiry_list = expiries()
    expiriesIteration(expiry_list)
    
    #print(x)
    #print(y)
    #print(z)

    return np.array(x), np.array(y), np.array(z)



