import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests

BASE_URL = 'https://kesko.azure-api.net'
SUBSCRIPTION_KEY = "bc5bbda6683e4c7bab9b06827fece364"
HEADERS = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
    }


def get_shops_in_area(params):
    conn = http.client.HTTPSConnection('kesko.azure-api.net')
    conn.request("POST", "/v1/search/stores?%s" % params, "{body}", HEADERS)
    response = conn.getresponse()
    # data = response.read()
    conn.close()
    return response


def get_params_for_nearest(lon, lat):
    # TODO -> Need to make this params correct form
    return urllib.parse.urlencode({
        "name": "distance",
        "location": {
            "lon": lon,
            "lat": lat
        }
    })
    return params


def get_params_for_area(lon, lat):
    # TODO -> Need to make this params correct form
    return urllib.parse.urlencode({
        "locationDistance": {
            "location": {
                "lon": lon,
                "lat": lat
            },
            "distance": 5
        }
    })


def get_product_in_store(params):
    url_string = BASE_URL + "/products/" + str(params["storeId"]) + "/" + str(params["ean"])

    r = requests.get(url_string, headers=HEADERS)
    response_json = r.json()
    return response_json
