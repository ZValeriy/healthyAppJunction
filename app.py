import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.route("/productInfo/<int:product_ean>")
def product_info(product_ean):
    return "Info about product"


@app.route("/productInfoStore/<int:product_ean>/<float:lon>/<float:lat>")
def product_info_store(product_ean, lon, lat):
    print("PRODUCT EAN: " + str(product_ean))
    print("LON: "+str(lon) + " LAT: "+ str(lat))
    return "GET INFO ABOUT PRODUCT IN STORE"

