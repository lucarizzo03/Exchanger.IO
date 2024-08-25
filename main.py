from api import getCountryRate
from func import multCountryRate, calcAmount


def main() :
    
    print("\n")
    print("Welcome to Exchanger \n")
    print("You can compare up to 3 currencies at the same time \n")
    print("These are some currencies you can compare: \n")
    print("USD - United States Dollar \n")
    print("EUR - Euro \n")
    print("GBP - British Pound Sterling \n")
    print("JPY - Japanese Yen \n")
    print("AUD - Australian Dollar \n")
    print("CAD - Canadian Dollar \n")
    print("CHF - Swiss Franc \n")
    print("CNY - Chinese Yuan \n")
    print("SEK - Swedish Krona \n")
    print("NZD - New Zealand Dollar \n")
    
    amount = int(input("Type how much money do you want to convert: "))
    numCurr = int(input("Type how many currencies you want to convert to: \n"))
    
    
    if numCurr < 2 :
        print("You are comparing 2 currencies \n")
        numCurr = 2
    elif numCurr > 3 :
        print("You are comparing 3 currencies \n")
        numCurr = 3
        

    if numCurr == 2 : 
        oneCurr = input("Type first currency: \n ")
        twoCurr = input("Type second currency: \n ")
        
        print("\n")
    
        rate = getCountryRate(oneCurr, twoCurr)
        convertAmount1 = calcAmount(rate, amount)

        print(f"The conversion of {amount} from {oneCurr} to {twoCurr} is {convertAmount1} \n")
        print(f"The exchange rate from {oneCurr} to {twoCurr} is {rate} {twoCurr}")
        
    elif numCurr == 3 :
        currs = []

        baseCurr = input("Type first currency: \n")
        secCurr = input("Type second currency: \n ")
        thiCurr = input("Type third currency: \n ")
        
        print("\n")
        
        currs.append(secCurr)
        currs.append(thiCurr)
        
        currs = multCountryRate(baseCurr, currs)
        secThirdConv = getCountryRate(secCurr, thiCurr)
        thirSecConc = getCountryRate(thiCurr, secCurr)
        
        sec_rate = currs.get(secCurr)
        third_rate = currs.get(thiCurr)
        
        convertedAmount2 = calcAmount(sec_rate, amount)
        convertedAmount3 = calcAmount(third_rate, amount)
        convertAmount4 = calcAmount(secThirdConv, amount)
        convertedAmount5 = calcAmount(thirSecConc, amount)
        
        
        
        print("\n")
        print("RESULTS: \n")
        print(f"The conversion of {amount} {baseCurr} to {secCurr} is {convertedAmount2} \n")
        print(f"The conversion of {amount} {baseCurr} to {thiCurr} is {convertedAmount3} \n")
        print(f"The conversion of {amount} {secCurr} to {thiCurr} is {convertAmount4} \n")
        print(f"The conversion of {amount} {thiCurr} to {secCurr} is {convertedAmount5} \n")
        
        print("\n")
        print("CONVERSION RATES: \n")
        print(f"The exchange rate between {baseCurr} and {secCurr}: {sec_rate}  {secCurr} \n")
        print(f"The exchange rate between {baseCurr} and {thiCurr}: {third_rate} {thiCurr} \n")
        print(f"The exchange rate between {secCurr} and {thiCurr}: {secThirdConv} {thiCurr} \n")
        print(f"The exchange rate between {thiCurr} and {secCurr}: {thirSecConc} {secCurr} \n")
        
        if (sec_rate > third_rate) :
            print(f"{secCurr} is greater than {thiCurr} when converting from {baseCurr}")
        else :
            print(f"{thiCurr} is greater than {secCurr} when converting from {baseCurr}")
            
    
    
    
            
    
    
    
            
            
            
            
            
        
    
    
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
   
        
    
    
            
        
        
        
    
if __name__ == "__main__" :
    main()       
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
