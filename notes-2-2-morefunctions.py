# More Functions
# Taylor Sayson
# 3 April 2024

# Implement star function

def stars(num):
    """Returns specified number of *s"""
    value = "" # place holder for return value


    # if number is 0, return 1 star
    # if number is 1, return 1 star
    # elif number is greater than 1, retrun that num * star
    # else return error saying negative number aren't allowed

    if num == 0 or num == 1:
        value = "*"
    elif num > 1:
        value = "*" * num
    else:
        value ="Sorry, can't take negative numbers."



    return value
print(stars(0))
print(stars(1))
print(stars(1000))
print(stars(-5))



# Multiply Strings 
greeting = "hello"
print(greeting * 5)

print("the quick brown fox jumps over the lazy dog" * 2)