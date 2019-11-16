from flask import Flask
import json
from flask import request
from get_shops import get_shops
from junc_API import get_product_in_store
from firebase_api.main_firebase import exists_in_firebase, Product

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.route("/productInfo")
def product_info_store():
    if request.args.get('ean'):
        product_ean = request.args.get('ean')

    if request.args.get('storeId'):
        store_id = request.args.get('storeId')
    else:
        store_id = 'N106'

    try:
        params = {
            "storeId": store_id,
            "ean": product_ean
        }

        response = get_product_in_store(params)
        # If we found something
        if response:
            if exists_in_firebase(product_ean):
                product = get_product_info(product_ean)
                return product, 201
            else:
                return {"ean": product_ean, "Name": response["name"]}, 200
    except Exception as e:
        return {"Code": "Error", "Message": e}, 404


@app.route("/addProduct")
def add_product():
    product = request.args.get('ingredients')
    new_product = Product(product["ingredients"], product["gluten_free"], product["vegan"],
                          product["package_type"], product["healthy"], product["ean"],
                          product["fats"], product["carbs"], product["proteins"], product["calories"],
                          product["name"], product["lacto"], product["sugar_free"])
    new_product.add_to_firebase()
    get_product_info(product_ean)
    return product, 201


@app.route("/getShops")
def get_shop_by_coord():

    try:
        lon = float(request.args.get('lon'))
        lat = float(request.args.get('lan'))
    except ValueError:
        return json.dumps({"Code": "Error", "Message": "Wrong coord type"})
    return json.dumps(get_shops(lon, lat))
