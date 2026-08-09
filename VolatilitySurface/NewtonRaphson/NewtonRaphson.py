from BlackScholes_.BlackScholes import BlackScholes, d1_
import math

def normal_pdf(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-(x ** 2) / 2)

def vega(S, d1, T):
    return S * normal_pdf(d1) * math.sqrt(T)

def price_error(Cbs, Cm):
    '''
    cost (market) and cost (using current IV and Black Scholes)
    '''
    return Cbs - Cm

def step(oldIV, E, Vega):
    '''
    step for iteration
    '''
    return (oldIV - (E / Vega))

def NewtonRaphson(S, K, T, r, Cm):
    '''
    Uses the Newton Raphson method (on the Black Scholes model) to iteratively solve for IV
    '''
    IV = 0.25 #initial guess
    tolerance = 0.000001
    max_iterations = 100

    for _ in range(max_iterations):
        d1 = d1_(S, K, T, r, IV)
        Cbs = BlackScholes(S, K, T, r, IV)
        E = price_error(Cbs, Cm)

        if abs(E) < tolerance:
            return IV

        Vega = vega(S, d1, T)
        
        if Vega == 0:
            raise ValueError("Vega is zero; Newton-Raphson cannot continue")
        

        IV = step(IV, E, Vega)
    
    raise ValueError("NewtonRaphson() failed to converge")


