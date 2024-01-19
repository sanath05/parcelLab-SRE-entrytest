# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet_customer():
    customer_name = request.args.get('customer_name', '')
    
    if customer_name.lower() == 'customer-A':
        greeting = 'Hi'
    elif customer_name.lower() == 'customer-B':
        greeting = 'Dear Sir or Madam'
    elif customer_name.lower() == 'customer-C':
        greeting = 'Moin'
    else:
        greeting = 'Hello'
    
    return jsonify({'greeting': greeting})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
