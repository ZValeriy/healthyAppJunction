from app import app
import json
from flask import request
from get_shops import get_shops_in_area
from junc_API import get_product_in_store
import urllib


@app.route("/productInfo")
def product_info():
    product_ean = request.args.get('ean')
    print(json.dumps({"ean": product_ean}))
    return json.dumps({"ean": product_ean})


@app.route("/productInfoStore")
def product_info_store():
    product_ean = request.args.get('ean')
    store_id = request.args.get('storeId', 'N106')

    try:
        params = urllib.parse.urlencode({
            "storeId": store_id,
            "ean": product_ean
        })

        response = get_product_in_store(params)
        # If we found something
        if response:
            response_data = response.read()
            return json.dumps({"Code": "Success", "Message": response_data}), 201
        else:
            return {"Code": "Success", "Message": "We found nothing, good day, sir"}, 404
    except Exception as e:
        return {"Code": "Error", "Message": e}, 404
