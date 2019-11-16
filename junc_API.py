import http.client, urllib.request, urllib.parse, urllib.error, base64
import sys
import app

SUBSCRIPTION_KEY = "bc5bbda6683e4c7bab9b06827fece364"


def get_shops_in_area(params):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
    }

    conn = http.client.HTTPSConnection('kesko.azure-api.net')
    conn.request("POST", "/v1/search/stores?%s" % params, "{body}", headers)
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
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
    }

    conn = http.client.HTTPSConnection('kesko.azure-api.net')
    urlString = "/products/"+str(params["storeId"]) + "/" + str(params["ean"])

    conn.request("GET", urlString, headers)

    response = conn.getresponse()
    conn.close()
    return response
