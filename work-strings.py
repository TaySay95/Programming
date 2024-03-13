# Strings Practice
# Taylor Sayson
# 9 Februrary 2024

import random

# Greet the user?
print()
print("Hello! 👋")

# Ask the user's name
print("What's your name?")
print()
name = input()

# Respond specifically to question
print()
print(f"Hi {name}!")

# Ask question 1
print("How are you doing? 🤔")
print()
feeling = input().lower()

# Respond specifically to question 1
print()
print(f"Oh, you're doing {feeling}? Interesting.")

# Ask question 2
print(f"How old are you, {name}?")
print()
age = input().capitalize()

# Respond specifically to question 2
print()
print(f"{age}, you say? That's cool. 👍")

# Ask question 3
print(f"What's your favourite colour, {name}?")
print()
colour = input().lower()

# Respond specifically to question 3

# Create if statements to choose emoji
if colour == "red":
    emoji = "🔴"
elif colour == "orange":
    emoji = "🟠"
elif colour == "yellow":
    emoji = "🟡"
elif colour == "green" or colour == "teal" or colour == "light green" or colour == "dark green":
    emoji = "🟢"
elif colour == "blue" or colour == "dark blue" or colour == "navy" or colour == "indigo":
    emoji = "🔵"
elif colour == "purple" or colour == "magenta" or colour == "violet":
    emoji = "🟣"
elif colour == "black":
    emoji = "⚫️"
elif colour == "white":
    emoji = "⚪️"
elif colour == "brown":
    emoji = "🟤"
elif colour == "pink":
    emoji = "🩷"
elif colour == "grey" or colour == "gray":
    emoji = "🩶"
elif colour == "light blue" or colour == "sky blue" or colour == "cyan":
    emoji = "🩵"
else:
    emoji = "🤔"

emojis = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "⚫️", "⚪️", "🟤", "🩷", "🩶", "🩵"]
capitalize_colour = colour.capitalize()

colour_responses = [f"I like {colour} too! {emoji}",
                    f"Cool! {capitalize_colour} is a nice colour. {emoji}", 
                    f"Oooh, {colour}. Nice choice! {emoji}",
                    f"{capitalize_colour} is a great choice! {emoji}",
                    f"{capitalize_colour} is a fantastic colour! {emoji}",
                    f"Good choice! I also like {colour} {emoji}!"]
colour_response = random.choice(colour_responses)

confused_responses = [f"{capitalize_colour} is an interesting choice. {emoji}",
                      f"Interesteing. Not too many people say that {colour} is their favourite colour. {emoji}",
                      f"{capitalize_colour}, you say? You are unique.",
                      f"Hmmm? {capitalize_colour} is a unique choice.",
                      f"Hmmm? {capitalize_colour} is a interesting choice."]
confused_response = random.choice(confused_responses)

print()
if emoji in emojis:
    print(colour_response)
else:
    print(confused_response)

# Say goodbye using the user's name
print()
print("Well, it was nice to meet you!")
print(f"Have a nice day, {name}. Goodbye! 👋")
