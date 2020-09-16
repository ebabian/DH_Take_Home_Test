import requests
from flask import Flask, render_template, request

# from flask_restful import Resource, Api

app = Flask(__name__)


# http://localhost:5000/
@app.route('/', methods=['GET'])
def index():
    ingredient_url = "https://raw.githubusercontent.com/daily-harvest/opportunities/master/web-1/data/ingredients.json"
    product_url = "https://raw.githubusercontent.com/daily-harvest/opportunities/master/web-1/data/products.json"

    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
    }

    products = []

    response = requests.get(ingredient_url)

    data = response.json()

    ingredient_ids = []
    for ingredient in data:
        ingredient_ids.append(ingredient['id'])
        print(ingredient_ids)

    product_response = requests.get(product_url)
    results = product_response.json()
    for product in results:
        product_data = {
            'id' : product['id'],
            'name' : product['name']
        }
        products.append(product_data)

    return render_template('index.html', products=products)

# Route: http://127.0.0.1:5000/ingredients/
# api.add_resource(IngredientList, '/ingredients/')

# if __name__ == '__main__':
# app.run(debug=True)

app.config["DEBUG"] = True
app.run()
