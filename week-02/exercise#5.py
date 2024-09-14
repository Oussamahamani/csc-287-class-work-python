favoriteFood = ["chicken","fish","pizza"]
foods= []
for food in favoriteFood:
    foods.append(food.lower())
print(foods)
print(foods[0:2])
print(foods[-1:-3])


foods.sort()
foods_upper = [food.upper() for food in foods]
print(foods_upper)
print([i for i in range(0,2)])