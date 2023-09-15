from tools import logger

import sys; print(sys.path)

recipes = []

with open("recipes.txt", "rt", encoding="utf8") as rec_fail:
    for text in rec_fail:
        dish_name = text.strip()
        dish = {"name": dish_name, "ingredients": []}
        ingredients_count = rec_fail.readline()
        for ing in range(int(ingredients_count)):
            ingredients = rec_fail.readline()
            name, quantity, measure = ingredients.strip().split(' | ')
            dish["ingredients"].append({"name": name, "quantity": quantity, "measure": measure})
        blank_line = rec_fail.readline()
        recipes.append(dish)

@logger('main.log')
def get_shop_list_by_dishes(list_dish, people):
    purchases = {}
    for dish in list_dish:
        for dish_book in recipes:
            if dish_book["name"] == dish:
                for ing in dish_book["ingredients"]:
                    if ing["name"] not in purchases.keys():
                        measure = ing["measure"]
                        quantity = people * int(ing["quantity"])
                        purchases[ing["name"]] = {"measure": measure, "quantity": quantity}

                    elif ing["name"] in purchases.keys():
                        measure = ing["measure"]
                        quantity = people * int(ing["quantity"]) + int((purchases[ing["name"]])["quantity"])
                        purchases[ing["name"]] = {"measure": measure, "quantity": quantity}
    return purchases

print(get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2))