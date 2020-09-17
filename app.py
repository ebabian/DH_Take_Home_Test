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

    # products array stores the product objects that contain the searched ingredients
    products = []

    if request.method == 'POST':
        # save searched ingredients to search_params['q']
        search_params = {
            'q': request.form.get('search')
        }

        response = requests.get(ingredient_url, params=search_params)

        data = response.json()

        # print(search_params['q'])

        # save ingredient objects to array if it exists in data
        ingredient_search = []

        # loop through data
        for ingredient in data:
            searched_ingredient = search_params['q']
            check_ingredient = ingredient['name']

            # if the searched ingredient, even if its a substring, is the same as an ingredient name
            if searched_ingredient.lower() in check_ingredient.lower():
                # store the ingredient's name and id to the ingredient search array
                ingredient_search.append(ingredient)
                print(ingredient_search[0])
                # print(ingredient_search[0]['id'])

        response = requests.get(product_url)
        data = response.json()
        # loop through the product API
        for product in data:
            # print(product['ingredientIds'])
            # loop through the ingredientIDs array in each product
            for ingredientID in product['ingredientIds']:
                # print(ingredientID)
                # if query search ID == product ingredientID then append Product match
                if ingredient_search[0]['id'] == ingredientID:
                    # only append the matches
                    products.append(product)
                    # print(products)

    return render_template('index.html', products=products)


app.config["DEBUG"] = True
app.run()
