import requests
from flask import Flask, render_template
from flask_restful import Resource, Api

url = "https://raw.githubusercontent.com/daily-harvest/opportunities/master/web-1/data/ingredients.json"
headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache"
}

response = requests.get(url, headers=headers)

data = response.json()

for ingredient in data:
        print (ingredient['id'])

# print(data)

app = Flask(__name__)
app.config["DEBUG"] = True

# class IngredientList(Resource):
# def get(self):
#       return data

# api = Api(app)

# http://localhost:5000/
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Route: http://127.0.0.1:5000/ingredients/
# api.add_resource(IngredientList, '/ingredients/')

# if __name__ == '__main__':
# app.run(debug=True)

app.run()
