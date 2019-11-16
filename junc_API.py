import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests
import json

BASE_URL = 'https://kesko.azure-api.net'
SUBSCRIPTION_KEY = "bc5bbda6683e4c7bab9b06827fece364"
HEADERS = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
    }


def get_shops_in_area(params):
    headers = {
        'Content-Type': 'raw',
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
    }
    url_string = "/v1/search/stores/"
    response = requests.post(BASE_URL + url_string, data=params, headers=headers)
    return response.json()


def get_params_for_nearest(lon, lat):
    return json.dumps({"filters": {
                            "sortOrders": {
                                "name": "distance",
                                "location": {
                                    "lon": float(lon),
                                    "lat": float(lat)
                                }
                            }
                        }
                    })


def get_product_in_store(params):
    url_string = BASE_URL + "/products/" + str(params["storeId"]) + "/" + str(params["ean"])

    r = requests.get(url_string, headers=HEADERS)
    response_json = r.json()
    return response_json
