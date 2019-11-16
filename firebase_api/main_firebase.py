import pyrebase
from acceptability_rating import get_product_description_and_rating

config = {
    "apiKey": "AIzaSyBjqAye_l6TLF-7XnIZFLMJaqI86CgdAVQ",
    "authDomain": "foddwaste.firebaseapp.com",
    "databaseURL": "https://foddwaste.firebaseio.com",
    "projectId": "foddwaste",
    "storageBucket": "foddwaste.appspot.com",
    "messagingSenderId": "714127414593",
    "appId": "1:714127414593:web:ae7996ccaae91ff0c17dc0"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


class Product:
    def __init__(self, ingredients, gluten_free, vegan, package_type, healthy, ean, carbs,
                 fats, proteins, calories, name, lacto, sugar_free):
        self.name = name
        self.ean = ean
        self.ingredients = ingredients  # array of strings
        self.vegan = vegan  # bool
        self.lacto = lacto  # bool
        self.gluten_free = gluten_free  # bool
        self.package_type = package_type
        self.healthy = healthy  # 1-3
        self.carbs = carbs
        self.fats = fats
        self.proteins = proteins
        self.calories = calories
        self.sugar_free = sugar_free  # bool

    def to_object(self):
        return {
            "name": self.name,
            "ingredients": self.ingredients,
            "vegan": self.vegan,
            "lacto": self.lacto,
            "glutenFree": self.gluten_free,
            "packageType": self.package_type,
            "healthy": self.healthy,
            "carbs": self.carbs,
            "fats": self.fats,
            "proteins": self.proteins,
            "calories": self.calories,
            "sugarFree": self.sugar_free
        }

    def add_to_firebase(self):
        db.child("products").child(str(self.ean)).set(self.to_object())


def exists_in_firebase(ean):
    product = db.child("products").child(ean).get()
    if product.val() is None:
        return False
    else:
        return True


def get_product_info(ean):
    product = db.child("products").child(ean).get()
    return dict(product.val())


def get_analogues(ean, user):
    product = get_product_info(ean)
    analogues = []
    for analog in product["analogues"]:
        analog_product = get_product_info(analog)
        analog_rating = get_product_description_and_rating(analog_product, user)["rating"]
        analogues.append({
            "ean": analog,
            "name": analog_product["name"],
            "rating": analog_rating
        })
    return analogues


def filter_by_parameter(parameter, products):
    return list(filter(lambda analog: analog[parameter], products))


def filter_analogues(analogues, user):
    analog_products = [get_product_info(analog["ean"]) for analog in analogues]
    filtered_analogues = analog_products
    if user["gluten_free"]:
        filtered_analogues = filter_by_parameter("glutenFree", filtered_analogues)
    if user["lacto"]:
        filtered_analogues = filter_by_parameter("lacto", filtered_analogues)
    if user["sugar_free"]:
        filtered_analogues = filter_by_parameter("sugarFree", filtered_analogues)
    if user["vegan"]:
        filtered_analogues = filter_by_parameter("vegan", filtered_analogues)
    
    return filtered_analogues
