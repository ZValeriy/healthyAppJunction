from junc_API import get_shops_in_area, get_params_for_nearest


def get_needed_shop_attributes(response):
    try:
        shop_id = response['results'][0]['Id']
        name = response['results'][0]['Name']
        address = response['results'][0]['Address']
        return {
                    "id": str(shop_id),
                    "name": str(name),
                    "address": str(address)
                }
    except Exception as e:
        return


def get_shops(lon, lat):
    try:
        params = get_params_for_nearest(lon, lat)
        response = get_shops_in_area(params)
        if response:
            shop_attrs = get_needed_shop_attributes(response)
            return {"Code": "Success", "Message": shop_attrs}, 201
    except Exception as e:
        return {"Code": "Error", "Message": e}, 404
