import requests
import json
from flask import Flask
app = Flask(__name__)



response = requests.get("https://data.cityofchicago.org/resource/4ijn-s7e5.json")

parsed = response.json()

@app.route('/')
def hello():
	return parsed

@app.route('/<name>')
def hello_name(name):
	return "Hello {}".format(name)

if __name__ == '__main__':
	app.run()

