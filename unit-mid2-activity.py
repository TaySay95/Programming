# Unit 2 Activity
# Taylor Sayson
# 10 April 2024 

# Create a file that includes 
# one custom function that has at least  one parameter and have a return value
# at least one loop, for or while

#  Create a bot that helps the user create study cards

def create():
    studycards = {}
    
    while True:
        print("Type in a term you want to add")
        term = input("ENTER TERM: ")
        print(f"Type the meaning of '{term}' ")
        definition = input(f"ENTER MEANING OF '{term}': ")
        studycards[term] = definition
            
        while True:        
            print("Do you want to add another flash card? (Y/N) ")
            answer = input("Answer: ").lower().strip(" .!/,")
            if answer == "y" or answer == "yes":
                break
            if answer == "n" or answer == "no":
                print("Now let's go through the flash cards you created!")
                return studycards
            else:
                print("Please enter a valid answer (Y/N)")
                
def review(deck):
    for a, b in deck.items():
        print("TERM:", a)
        input("Press the ENTER key to reveal the definition.")
        print("DEFINITION:", b)
        input("Press ENTER key to proceed.")
    print("That is the end of the set of flashcards")
        
        
def main():
    print("Hello, I am study bot! I can help you create study cards for any upcoming quiz or test")
    print("To begin, let's create a title for your study cards.")
    title = input("TITLE: ").upper()

    print(f"Thank you, now we will add questions to your {title} flash card set")


    
    
    x = create()
    review(x)  
    while True:
        print("Do you want to go over the flash cards again? (Y/N)")
        again = input().lower().strip(" .!/,")
        if again == "y" or again == "yes":
            print(f"Sounds good, let's go over '{title}' again!")
            review(x)
        if again == "n" or again == "no":
            print("Okay then. Thank you for using study bot today!")
            break
        else:
            print("Please enter a valid answer (Y/N)")
        
main()