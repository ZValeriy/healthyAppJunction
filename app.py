from flask import Flask
import json
from flask import request

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.route("/productInfo")
def product_info():
    product_ean = request.args.get('ean')
    print(json.dumps({"ean": product_ean}))
    return json.dumps({"ean": product_ean})


@app.route("/productInfoStore")
def product_info_store():
    product_ean = request.args.get('ean')
    longitude = request.args.get('lon')
    latitude = request.args.get('lan')

    return json.dumps({"ean": product_ean, "lon": longitude, "lan": latitude})

