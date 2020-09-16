import requests
from flask import Flask, render_template, request

# from flask_restful import Resource, Api

app = Flask(__name__)


# http://localhost:5000/
@app.route('/', methods=['GET', 'POST'])
def index():
    ingredient_url = "https://raw.githubusercontent.com/daily-harvest/opportunities/master/web-1/data/ingredients.json"
    product_url = "https://raw.githubusercontent.com/daily-harvest/opportunities/master/web-1/data/products.json"

    # headers = {
    # 'Content-Type': "application/json",
    # 'Cache-Control': "no-cache"
    # }

    products = []

    if request.method == 'POST':
        search_params = {
            'q': request.form.get('search')
        }
        response = requests.get(ingredient_url, params=search_params)

        data = response.json()

        print(search_params['q'])
        ingredient_search = []
        for ingredient in data:
            # if the search ingredient is the same as an ingredient name
            if search_params['q'] == ingredient['name']:
                # store the ingredient's name and id to the ingredient search array
                ingredient_search.append(ingredient)
                # print(ingredient_search)


        response = requests.get(product_url)
        data = response.json()
            # take user input and loop through the product ingredientID
            # if query search ID === product ingredientID then append Product match
        for product in data:
            if ingredient_search[0]['id'] == product['ingredientIds']:
                # only append the matches
                products.append(product['name'])
                print(products)

    return render_template('index.html', products=products)


app.config["DEBUG"] = True
app.run()
