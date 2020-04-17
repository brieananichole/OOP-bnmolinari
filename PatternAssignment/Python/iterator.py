def favorite_breakfast(count):
    #lists my favorite breakfast foods in order, eggs being number one and sausage being number 5

    breakfastItems = ["eggs", "bacon", "pancakes", "waffles", "sausage"]

    # The zip keeps from counting over the limit
    for number, pos in zip(breakfastItems, range(count)):
        yield number

top_3_foods = lambda : favorite_breakfast(3)
top_5_foods = lambda : favorite_breakfast(5)

print("My top 3 breakfast foods are…")
for number in top_3_foods():
    print(number),
print("\n")
print ("My top five breakfast foods are…")
for number in top_5_foods():
    print(number),