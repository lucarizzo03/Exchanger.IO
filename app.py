from flask import Flask, request, jsonify, render_template
from api import getCountryRate, multCountryRate, calcAmount

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    print(data)
    
    # Provide default values and handle possible missing keys
    amount = float(data.get('amount', 0))
    base_currency = data.get('base_currency', 'USD')
    num_currencies = int(data.get('num_currencies', 0))
    target_currencies = data.get('target_currencies', [])
    
    results = {}
    
    if len(target_currencies) > 0:
        if len(target_currencies) == 1:
            rate = getCountryRate(base_currency, target_currencies[0])
            converted_amount = calcAmount(rate, amount)
            results[target_currencies[0]] = {'rate': rate, 'converted_amount': converted_amount}
        elif len(target_currencies) > 1:
            rates = multCountryRate(base_currency, target_currencies)
            for currency in target_currencies:
                rate = rates.get(currency, 0)
                converted_amount = calcAmount(rate, amount)
                results[currency] = {'rate': rate, 'converted_amount': converted_amount}

    
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
