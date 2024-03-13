# Answer to the Great Question
# Taylor Sayson
# 20 February 2024

# Ask what the meaning of life? Recording input case insensitively
response = input("What is the meaning of life? ").lower()

# write if statement responding yes if response is 42 or no if not
if response == "42" or response == "forty-two" or response == "forty two":
    print("Yes")
else:
    print("No")