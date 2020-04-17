def favorite_breakfast(count):
    #lists my favorite breakfast foods in order, eggs being number one and sausage being number 5

    breakfastItems = ["eggs", "bacon", "pancakes", "waffles", "sausage"]

    # The zip keeps from counting over the limit
    for food, pos in zip(breakfastItems, range(count)):
        yield food

top_3_foods = lambda : favorite_breakfast(3)
top_5_foods = lambda : favorite_breakfast(5)

print("My top 3 breakfast foods are…")
for food in top_3_foods():
    print(food),
print("\n")
print ("My top five breakfast foods are…")
for food in top_5_foods():
    print(food),