# Loops and Iteration
# Taylor Sayson
# 5 April 2024

# # Print "something" 10 times
# for _ in range(100000000):
#     print("something")

#print out every item in my grocery list
grocery_list = [
    "dishwasher tabs",
    "aluminum foil",
    "blueberry muffins",
    "drinks"
]

for item in grocery_list:
    print("-----")
    print(f"* {item}")

    if item =="blueberry muffins":
        break

#count from 0-9
for i in range(100):
    print(i)
    # Modulo
    if i % 2 == 1:
        print(f"{i} is an even number")


# Rewrite the above for loop as a while loop
counter= 0
while counter < 100:
    print(counter)
    # counter = counter + 1 or
    counter+= 1