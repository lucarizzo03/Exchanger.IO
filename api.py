import requests
from config import HOME_URL


# grabs coverison rates between two currencies using API endpoint 
def getCountryRate(fromCurr, toCurr) :
   
    # making request url
    url = f"{HOME_URL}/{fromCurr}?symbols={toCurr}"
    
    # making call to api
    apiReq = requests.get(url)
    
    # parses api request data
    data = apiReq.json()
    
    # accesses the value within the data 
    exchangeRate = data['rates'].get(toCurr)
    
    return exchangeRate



    
    
    
    
        

        
        
    

    
    
    
