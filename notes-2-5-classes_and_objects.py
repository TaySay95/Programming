# Taylor Sayson
# Classes and Objects
# 15 April 2024

# Big Ideas

# Create a class thgat represents a Pokemon
class Pokemon: # always name classes with capital
    def __init__(self):
        """Constructor contain all properties of a Pokemon
        """
        self.name = ""
        self.id = 0
        self.weight = 0
        self.height = 0
        self.type = "Normal"

def main():
    # Create two Pokemon:

    # Create something 'Pikachu'-like
    pokemon_one = Pokemon()
    pokemon_one.name = "Pikachu"
    pokemon_one.type = "Electric"
    pokemon_one.id = 25

    #print values of pokemon_one
    print(pokemon_one.name)
    print(pokemon_one.type)



    # Create something 'Squirtle'-like
    # TODO: Create squirtleliek
    #- Create a new pokemon object
    #store this is variable pokemon_two
    #squirltes pokede id is 4
    # squirtles's tuype is water
    pokemon_two = Pokemon()
    pokemon_two.name = "Squirtle"
    pokemon_two.id = 4
    pokemon_two.type = "Water"

    print(pokemon_two.name)
    print(pokemon_two.type)
    print(pokemon_two.id)

if __name__ == "__main__":
    main()