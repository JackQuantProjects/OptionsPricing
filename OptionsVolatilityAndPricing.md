---
id: OptionsVolatilityAndPricing
aliases: []
tags: []
---

# Options pricing and volatility

## Derivatives

Spot/Cash - an "almost" immediate exchange of cash for goods

Forward contract - an agreed upon spot that will take place in the future

futures contract - a standardised forward where the exchange (middle man) guarantees that the contract is fulfilled

Options contract - gives one party the option to exit the contract with no guilt. this comes at the cost of a premium

Call option - buyer has the right to buy the underlying

Put option - buyer has the right to sell the underlying

Swap - an agreement to "swap" cash flows. example: fixed interest rate to floating interest rate.

## Pricing Forwards

forwards price - current cash price + cost of buying now - benefits of buying now

basis - the difference between the forward and the spot price

### Physical commodities

- C = price of commodities
- t = time till maturity
- r = interest rate
- S = storage price
- i = insurance price

$$
F = C * (1 + (r * t)) + (S + i)t
$$

### Stock

- S = stock price
- t = time till maturity
- i = interest rate
- $d_i$ = each dividend expected prior to maturity
- $t_i$ = time till maturity after each dividend payment
- $r_i$ = the applicable interest rate from each dividend payment 

$$
F = S + (S * r * t) - \sum [d_n * (1 + r_n * t_n)]
$$

### Bonds and Notes

- B = bond price
- t = time till maturity
- $c_i$ = each coupon expected prior to maturity
- $t_i$ = time til maturity after each coupon
- $r_i$ = interest rate for each coupon

$$
F = B + (B * r * t) - \sum [c_n * (1 + r_n * t_n)]
$$

### Foreign currencies

- S = spot exchange rate
- $c_d$ = 1 domestic currency unit
- $c_f$ = 1 foreign currency unit
- $r_d$ = domestic interest rate
- $r_f$ = foreign interest rate

$$
F = S * (\frac{1 + r_d * t}{1 + r_f * t})
$$



Forward price formula can be rearranged to find implied values for other variables

## Dividends

Declared date - date when the company announces the amount of the dividend and the date the dividend will be paid

Record date - the date in which the stock had to be owned before to qualify for the dividend

Ex-div date - the first day of trading without qualifying for the dividend

payable date - the date in which the dividend will be paid

Locked futures - when the futures daily price limit is reached no more futures trading may take place

borrowed stock still "belongs" to the lender and therefore any dividends must be paid to the lender

the loaner can benefit by only paying part of the interest that the borrower is due. this amount is determined by how hard it is to borrow the stock

## Contract Specification - Option terminology

The buyer of an option gets the choice of whether the option is a call or a put type option

The underlying is the commodity to be brought/sold

mid-curve option - short term option on long term futures

____-year mid curve is a short term option on a ____-year future

expiration date is the date where you must decide on the option

exercising an option means to go through with the buy/sell

being assigned means that you are required to sell/buy at the exercise price

##### exercise style:
- European - decision on final day
- American - decision any time before expiration


the intrinsic value of an option is the difference in the stock price and the option exercise price (always +)

the time-value or extrinsic value is the value of the length of the option

the intrinsic and extrinsic value must sum to the options premium

if an option is trading at parity it means the time value equals 0

in the money means that the option has a positive intrinsic value 

out the money means the option has zero intrinsic value

at the money means the option is trading at parity

automatic exercise - if no exercise notice is given exchanges will auto exercise any in the money contracts above the transactional costs

SPAN - Standard Portfolio Analysis of Risk
-> the most widely used margining system on futures exchanges

## Probability and theoretical pricing

expected value = mean or average

edge = the difference in buy in and expected return when the buy in is less than the return (eventual loss for buyer)

theoretical value = the price a bet should be in order to break even in the long run

if a business has a price slightly edged above the theoretical value it must be able to withstand the unlucky periods to see eventual long term growth

models are guides to things and should not be treated with 100% trusted 

theoretical value must equal the forward price to prevent an arbitrage opportunity

models become less accurate closer to the expiration date

liquid - when the bid ask spread is narrow

risk free rate - the interest rate at the most trustworthy borrower

a more realistic rate that the risk free rate is the LIBOR or euro-currency markets

should only account for dividends if the ex-dividend date is before the options expiery

## Volatility

Volatility is the speed in which the market moves 

a higher volatility increases the values of options

estimates from $\sigma$ on a normal distribution

- +-1 ~ 68.3%
- +-2 ~ 95.4%
- +-3 ~ 99.7%

volatility is thought of in a % annually

if we wish to convert to shorter time periods we must do so with the square root of time

realised volatility - volatility calculated using historical data

implied volatility - volatility derived from an options market value assuming that all inputs are known and correct

inputs must be contemporaneous from a similar point in time

premium and implied volatility can be used interchangeably

at or out of the money options are the most sensitive to volatility changes due to having 0 intrinsic value and are therefore more frequently traded than in the money options

the longer term the option, the greater the effect volatility changes will have

## Risk Measurment

options' value can depend on the traders current position.

traders should avoid short stock positions whenever possible

### The Greeks:

Delta ($\Delta$) the rate of change with respect to the underlying 

rate of change  - how quickly the option value changes with respect to the underlings movement 

hedge ratio - the number of underlying contracts needed for a riskless hedge using the delta (100/$\Delta$)

probability - the delta can act as an estimate for the probability that an option expires in the money however, not commonly used like this due to the lack if indication of how far into the money

Gamma ($\Gamma$) - the rate of change of the delta per point in the underlying. when the underlying changes by 1 point the gamma is added or subtracted from the old delta to give a new delta.

Theta ($\theta$) - time decay. the rate at which an option looses its value per day

vega/kappa (K) - the option's price's sensitivity to volatility per 1% change in volatility

Rho (P) - an option's price's sensitivity to interest per 1%

when used in FX Phi ($\phi$) is substituted for Rho

when trading an option, to better realise out theoretical edge we can break it into many smaller time frame bets.

for example: a 10 weeks option can be re-hedged to delta neutral every week turning it into 10 small bets

returning to delta neutral is called adjustment

the profit gained from this option will be the result of the sum of the adjustments of the period of the option

there are two approches to this: re-hedge at a time interval or re-hedge when the delta position strays by a certain amount from neutral.

Higher volatility means more profit. Lower equals less

break-even probability = probability for the profit to be zero

this is the same as implied volatility from an options price

vanna - the deltas sensitivity to volatility

charm / delta decay - deltas sensitivity to time
