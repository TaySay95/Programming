# Text/Emoji Replacer
# Taylor Sayson
# 26 February 2024

# Create a function called translate
# Accepts a string as parameter
# From the parameter replace all 100 with emoji and all noodles with emoji
    # str.replace(old, new)
    # Returns a copy of the string with all occurrences of substring old replaced by new. 
# Return the result

def translate(user_input: str):
    user_input = user_input.replace("100", "💯")
    user_input = user_input.replace("noodles", "🍜")
    return user_input

# Define main
# Gather input
def main():
    data = input("Say something about noodles or 100: ")
    print(translate(data))
    
# Run main()
main()

