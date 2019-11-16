from flask import Flask
import json
from flask import request

from junc_API import get_product_in_store

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
            return response, 201
        else:
            return {"Code": "Success", "Message": "We found nothing, good day, sir"}, 404
    except Exception as e:
        return {"Code": "Error", "Message": e}, 404
