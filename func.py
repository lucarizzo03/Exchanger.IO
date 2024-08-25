from api import getCountryRate

# used for when comparing 3 currencies 
def multCountryRate(baseCurr, currencies) :
    rates = {}
    
    for exRate in currencies :
        result = getCountryRate(baseCurr, exRate)
        rates[exRate] = result
        
    return rates 

# returns base amount converted from currency 
def calcAmount(rate, baseAmount) :
    toCurr = rate * baseAmount
    
    return toCurr