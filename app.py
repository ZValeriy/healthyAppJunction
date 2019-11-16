from flask import Flask
import json
from flask import request

from junc_API import get_product_in_store

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
    store_id = request.args.get('storeId')

    try:
        params = {
            "storeId": store_id,
            "ean": product_ean
        }

        response = get_product_in_store(params)
        # If we found something
        if response:
            return response, 201
        else:
            return {"Code": "Success", "Message": "We found nothing, good day, sir"}, 404
    except Exception as e:
        return {"Code": "Error", "Message": e}, 404
