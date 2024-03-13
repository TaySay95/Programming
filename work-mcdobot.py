# McDoBot
# Taylor Sayson
# 21 February 2024

answer = input("Would you like fries with your meal? (Yes/No) ")

if answer.strip(" !?./,'").lower() == "yes":
    print("Here is your meal with fries!")
elif answer.strip(" !?./,'").lower() == "no":
    print("Here is your meal without fries!")
else:
    print(f"""Sorry, I didn't understand "{answer.strip()}".""")