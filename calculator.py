"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# Forever loop
while True:
    # Grab input from user
    input_string = input('Write your equation > ')

    #Tokenize input
    tokens = input_string.split(' ')

    # Let the user quit with 'q'
    if tokens[0] == 'q':
        quit()
    # Else, execute the proper math function
    else:
        # Call pow function if first token matches 'pow'
        if tokens[0] == 'pow':
            print(power(int(tokens[1]), int(tokens[2])))
        # Call add function if first token matches '+'
        if tokens[0] == '+':
            print(add(int(tokens[1]), int(tokens[2])))
        # Call divide function if first token matches '/'
        if tokens[0] == '/':
            print(divide(int(tokens[1]), int(tokens[2])))
        