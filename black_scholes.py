import numpy as np 
from scipy.stats import norm


#parameter 
""" Short term Interest rates -  r
    t - maturity date (days/365)
    x - underlying price
    s - strike price
    v = volatality (in decimal)

"""

def blackScholes(r,x,s,t, v, type = 'Call'):
    t = t/365
    d1 = (np.log(x/s) + (r + v**2/2)*t)/(v*np.sqrt(t))
    d2 = d1 - v*np.sqrt(t)

    try:
        if type == 'Call':
            price = x*norm.cdf(d1, 0, 1) - s*np.exp(-r*t)*norm.cdf(d2,0,1)
        elif type == 'Put':
            price = s*np.exp(-r*t)*norm.cdf(-d2,0,1) - x*norm.cdf(-d1, 0, 1)
        return price


    except:
        print("Confirm all Parameters are entered correctly!!")



t = int(input("days: "))
x = int(input ("current price: "))
s = int(input("strike price: "))
v = float(input("What is the volatality: "))
r = float(input("risk free interest rate: "))

print("expected put price is" , round(blackScholes(r,x,s,t,v,'Put'),2))
print("expected call price is" , round(blackScholes(r,x,s,t,v,'Call'),2))
