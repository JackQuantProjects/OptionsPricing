import numpy as np
import pandas as pd
import math
from statistics import NormalDist
import pytest

# Black Scholes model

def d1_(S, K, T, r, IV):
    '''
    how many standard deviations the strike price is from the mean
    '''
    top = (math.log(S/K) + ((r + ((IV**2) / 2)) * T))
    bottom = (IV * math.sqrt(T))
    return (top)/(bottom)


def d2_(d1, IV, T):
    '''
    adjusted standardised distance from the strike 
    '''
    return (d1 - (IV * math.sqrt(T)))


def N(x):
    return NormalDist().cdf(x)


def C(S, K, T, r, IV, d1, d2):
    '''
    C =  E(profit) - E(cost)

    using log-normal dist:
    E(profit) = sum of all values about strike / number
    E(cost) = sum of all values below strike / number

    '''
    return ( S * N(d1) ) - ( (K) * (math.e ** (-r * T)) * (N(d2)) )

def BlackScholes(S, K, T, r, IV):
    d1 = d1_(S, K, T, r, IV)

    d2 = d2_(d1, IV, T)

    return C(S, K, T, r, IV, d1, d2)
