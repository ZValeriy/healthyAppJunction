# from firebase_api.main_firebase import Product
# import pyrebase
# import random
#
# config = {
#     "apiKey": "AIzaSyBjqAye_l6TLF-7XnIZFLMJaqI86CgdAVQ",
#     "authDomain": "foddwaste.firebaseapp.com",
#     "databaseURL": "https://foddwaste.firebaseio.com",
#     "projectId": "foddwaste",
#     "storageBucket": "foddwaste.appspot.com",
#     "messagingSenderId": "714127414593",
#     "appId": "1:714127414593:web:ae7996ccaae91ff0c17dc0"
# }
#
# firebase = pyrebase.initialize_app(config)
# db = firebase.database()
#
# packageTypes = ["metal", "plastic", "paper", "glass", "cloth", "mix"]
#
# products = db.child("products").get().val()
# for key in products.keys():
#     analogues = []
#     for i in range(5):
#         name = "An. №" + str(i) + " for " + products[key]["name"]
#         carbs, prots, fats, cals, healthy, ean = random.randint(0, 20), random.randint(5, 25), random.randint(1, 25), \
#                                                  random.randint(150, 500), random.randint(2, 5), \
#                                                  random.randint(6000000000000, 9999999999999)
#         lacto, sugar, vegan, gluten = bool(random.randint(0, 1)), bool(random.randint(0, 1)), bool(random.randint(0, 1)), \
#                                       bool(random.randint(0, 1))
#         material = packageTypes[random.randint(0, 5)]
#         ingredients = ["ingr", "ingredients"]
#         analogues.append(ean)
#         product = Product(ingredients, gluten, vegan, material, healthy, ean, carbs, fats, prots, cals, name, lacto,
#                           sugar)
#         product.add_to_firebase()
#     for analogue in analogues:
#         new_analogues = analogues.copy()
#         new_analogues.remove(analogue)
#         new_analogues.append(key)
#         db.child("products").child(analogue).update({"analogues": new_analogues})
#     db.child("products").child(key).update({"analogues": analogues})
#
# for key in products.keys():
#     analogues = products[key]["analogues"]
#     new_analogues = []
#     for analogue in analogues:
#         new_analogues.append(str(analogue))
#     db.child("products").child(key).update({"analogues": new_analogues})