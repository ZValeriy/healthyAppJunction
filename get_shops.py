from junc_API import get_shops_in_area, get_params_for_area, get_params_for_nearest
from app import app


@app.route("/get_shops/<lon>/<lat>")
def get(lon, lat):
    # Trying to get shops around the area
    try:
        params = get_params_for_area(lon, lat)
        response = self.get_shops_in_area(params)
        # If we found something
        if response:
            return {"Code": "Success", "Message": response}, 201
        # If we don`t found any shops around the area, then try to find nearest
        else:
            params = get_params_for_nearest(lon, lat)
            response = self.get_shops_in_area(params)
            return {"Code": "Success", "Message": response}, 201 if response \
                else {"Code": "Success", "Message": "We found nothing, good day, sir"}, 201
    except Exception as e:
        return {"Code": "Error", "Message": e}, 404

