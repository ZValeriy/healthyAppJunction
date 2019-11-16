def get_gluten(product, dude):
    if dude["gluten_free"] and not product["gluten_free"]:
        return "Product include gluten, you shouldn`t eat it."
    return ''

def get_lacto(product, dude):
    if dude["lacto"] and product["lacto"]:
        return "Product include lactose, you shouldn`t eat it."
    return ''

def get_vegan(product, dude):
    if dude["vegan"] and not product["vegan"]:
        return "Product isn`t vegan, you shouldn`t eat it."
    return ''

def get_sugar(product, dude):
    if dude["sugar_free"] and not product["sugar_free"]:
        return "Product include sugar, you shouldn`t eat it."
    return ''

def get_allergic(product, dude):
    allergic_ingredients = list(set(dude["allergic_ingredients"]).intersection(set(product["ingredients"])))
    if len(allergic_ingredients) > 2:
        allergic_ingredients = allergic_ingredients[:2]
    if len(allergic_ingredients) > 0:
        return "Product include " + ", ".join(allergic_ingredients) + ", you shouldn`t eat."
    return ''

def get_general_product_info(product):
    warning_message = ''
    rating = 0
    if float(product["fats"]) > 30:
        warning_message = "Product not so healthy"
        rating = 2

    elif float(product["fats"]) > 20 and float(product["fats"]) < 30:
        warning_message = "Product is normal"
        rating = 3

    elif float(product["fats"]) < 20:
        warning_message = "Product is quite good"
        rating = 4
    
    return warning_message, rating


def get_product_description_and_rating(product, dude):
    rating = 0
    warning_message = {
        "gluten": get_gluten(product, dude),
        "lacto": get_lacto(product, dude),
        "vegan": get_vegan(product, dude),
        "sugar": get_sugar(product, dude),
        "allergic": get_allergic(product, dude)
    }

    for key in warning_message.keys():
        if warning_message[key]:
            rating = 1
            break

    if not rating and product["healthy"] == 5:
        rating = 5
        warning_message["general"] = "This product is nice for you, bon appétit"
        return {"rating": rating, "warning_message": warning_message}

    if not rating:
        warning_message["general"], rating = get_general_product_info(product)
    
    return {"rating": rating, "warning_message": warning_message}
