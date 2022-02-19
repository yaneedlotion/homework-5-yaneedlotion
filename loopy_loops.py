


if __name__ == "__main__":

    pokemon = "pikachu", "charmander", "bulbasaur"
    pikachu, charmander, bulbasaur = pokemon
    first_tuple = tuple(pokemon)
    print(pokemon)
    print(f'starter1: ' + (pikachu))
    print(f'starter2: ' + (charmander))
    print(f'starter3: ' + (bulbasaur))

    name = input('')
    name = tuple(name)
    print(name)

    letter = ('i')
    print(f'"{letter}" is in name?: {letter in name}')
    
    for i in range(2, 11):
        print(i)

    numbers = range(2, 11)

    i = 0
    while i < len(numbers):
        print(numbers[i])
        i += 1

    simple_string = 'This is a simple string'
    for letter in simple_string:
        print(letter)

    simple_set = ('this', 'is', 'a', 'simple', 'set')
    for i in simple_set:
        for word in simple_set:
            print(f'{i * 3}; {word * 3}')