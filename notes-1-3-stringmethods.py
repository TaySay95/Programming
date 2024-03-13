# Methods- String Methods
# Taylor Sayson
# 21 February 2024

# Ask the user what the weather is
user_reply = input("What is the weather like? ").strip(" !.?").lower()
# If they answer rainy say: Bring an umbrella 

if user_reply == "rainy":
    print("Bring an umbrella!")
else:
    print("Sorry, I didn't understand what you said")