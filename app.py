import requests
from flask import Flask
from flask_restful import Resource, Api, reqparse

url = "https://raw.githubusercontent.com/daily-harvest/opportunities/master/web-1/data/ingredients.json"
headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
        }

response = requests.get(url, headers=headers)

data = response.json()

print(data)

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

class IngredientList(Resource):
        def get(self):
                return data

api.add_resource(IngredientList, '/ingredients/')

if __name__ == '__main__':
        app.run(debug=True)