import pyrebase
import json

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
        print("NOO")
        return False
    else:
        print("YAP")
        return True


exists_in_firebase(9711248272)
