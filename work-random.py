

import random
def card_reveal():
    roll = random.randrange(1,14)
    if roll == 1:
        return "A"
    elif roll == 11:
        return "J"
    elif roll == 12:
        return "Q"
    elif roll == 13:
        return "K"
    else:
        return str(roll)

def main():
    print(card_reveal())

main()
