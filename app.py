from flask import Flask
import json
from flask import request
from get_shops import get_shops
from junc_API import get_product_in_store
from firebase_api.main_firebase import exists_in_firebase, Product, get_product_info
from acceptability_rating import get_product_description_and_rating

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.route("/productInfo", methods=["POST"])
def product_info_store():

    if request.form.get("ean"):
        product_ean = request.form.get("ean")

    if request.form.get("storeId"):
        store_id = request.form.get("storeId")
    else:
        store_id = 'N106'

    user = request.form.get("user")

    try:
        params = {
            "storeId": store_id,
            "ean": product_ean
        }

        response = get_product_in_store(params)
        # If we found something
        if response:
            print(product_ean)
            if exists_in_firebase(product_ean):
                product = get_product_info(product_ean)
                print(product)
                product_info = get_product_description_and_rating(product, user)
                print(product_info)
                return product_info, 201
            else:
                return {"ean": product_ean, "name": response["name"]}, 200
        else:
            return {}, 202
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
    return {"Status": "Success"}, 201


@app.route("/getShops")
def get_shop_by_coord():

    try:
        lon = float(request.args.get('lon'))
        lat = float(request.args.get('lan'))
    except ValueError:
        return json.dumps({"Code": "Error", "Message": "Wrong coord type"})
    return json.dumps(get_shops(lon, lat))
