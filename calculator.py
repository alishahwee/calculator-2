"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# Forever loop
while True:

    # Initialize validity to be false
    input_validity = False

    # Reprompt user until their input is valid
    while input_validity is not True:
        # Grab input from user
        input_string = input('Write your equation > ')
        # Tokenize input
        tokens = input_string.split(' ')
        
        # Let the user quit with 'q'
        if tokens[0] == 'q':
            quit()
        # Evaluate input for validity
        try:
            if type(tokens[0]) is str and type(int(tokens[1])) is int and type(int(tokens[2])) is int:
                # Reinitialize validity to be true
                input_validity = True
            
                # Call pow function if first token matches 'pow'
                if tokens[0] == 'pow':
                    print(power(int(tokens[1]), int(tokens[2])))
                # Call add function if first token matches '+'
                if tokens[0] == '+':
                    print(add(int(tokens[1]), int(tokens[2])))
                # Call divide function if first token matches '/'
                if tokens[0] == '/':
                    print(divide(int(tokens[1]), int(tokens[2])))
                # Call subtract function if first token matches '-'
                if tokens[0] == '-':
                    print(subtract(int(tokens[1]), int(tokens[2])))
                # Call multiply function if first token matches '*'
                if tokens[0] == '*':
                    print(multiply(int(tokens[1]), int(tokens[2])))
                # Call square function if first token matches 'square'
                if tokens[0] == 'square':
                    print(square(int(tokens[1])))
                # Call cube function if first token matches 'cube'
                if tokens[0] == 'cube':
                    print(cube(int(tokens[1])))
                # Call mod function if first token matches 'mod'
                if tokens[0] == 'mod':
                    print(mod(int(tokens[1]), int(tokens[2])))
        except:
            print('You have to use prefix notation.')

            