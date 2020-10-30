import array


bread_types = ["Yeast bread","Flatbread","Rye"]
cheese_types = ["Cheddar","Gouda","Goat cheese"]
meat_types = ["Beef meat","chicken", "Goat meat"]

def odds_meals(bread_types,cheese_types, meat_types):
    meals = []
    i = 0
    for bread in bread_types:
        for cheese in cheese_types:
            for meat in meat_types:
                meals.insert(i,[bread,cheese,meat])
                i +=1
    return meals


#print(odds_meals(bread_types,cheese_types,meat_types))

meals = odds_meals(bread_types,cheese_types,meat_types)
print(type(meals))
print(len(meals))
