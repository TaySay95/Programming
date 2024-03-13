# Chatbot
# Taylor Sayson
# 8 March 2024

import random

# # 1. Greets the user
# print("Hello there!")

# # 2. Asks them, "how are you?" or something like it
# print("How are you doing?")
# user_feeling = input().strip(",.?! ").lower()

# # 3. Responds with a general statement
# #       that is randomly chosen
# #         - create a list of possible responses
# #         - randomly choose a response
# #         - print that response

# good_possible_resp = [
#     "I'm really happy for you.",
#     "That's really good news!!",
#     "That's awesome.",
# ]
# bad_possible_resp = ["I'm sorry you're feeling that way.", "There, there.", "🥺"]
# neutral_possible_resp = ["Thanks for sharing that with me.", "Cool!", "🤜🤛"]

# if user_feeling == "good" or user_feeling == "great":
#     print(random.choice(good_possible_resp))
# elif user_feeling == "bad" or user_feeling == "not too good":
#     print(random.choice(bad_possible_resp))
# else:
#     print(random.choice(neutral_possible_resp))

# # 4. Says goodbye
# print("Well thank you for your time! 😊")

def coinflip():
    # return heads, tails or other
    # Heads is any number 0 to 0.4999999
    # Tails is any number from 0.5 to 0.999991
    # Other is 0.999991 to 1
    roll = random.random()
    if roll < 0.5:
        return "heads"
    elif roll < 0.999999:
        return "tails"
    else:
        return "other"
    


def main():
    # keep track of heads and tails
    heads = 0
    tails = 0
    other = 0 
    for _ in range(1000000):
        result = coinflip()
        if result == "heads": 
            heads = heads + 1 #increment
        elif result == "tails":
            tails += 1 #increment
        else:
            other += 1

    #print results()
    print(f"Number of Heads: {heads}")
    print(f"Number of Tails: {tails}")
    print(f"Number of Other: {other}")

main()

