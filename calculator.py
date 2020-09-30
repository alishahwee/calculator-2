"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# Forever loop
while True:
    # Grab input from user
    input_string = input('Write your equation > ')

    #Tokenize input
    tokens = input_string.split(' ')
