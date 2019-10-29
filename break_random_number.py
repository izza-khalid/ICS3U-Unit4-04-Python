#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: October 2019
# This program breaks loop when random number guessed correctly
# with user input

import random
some_variable = random.randint(1, 10)
# a number between 1 and 10


def main():
    # This function breaks loop when random number guessed correctly
    counter = 0

    # input
    print("Quick! Pick a number between 0 and 10")
    print("")

    while True:
        print("")
        your_number = int(input("Enter the number of your choice: "))
    # process & output
        if your_number == some_variable:
            print("You got it right!!!")
            break
        else:
            print("Lets try again!")


if __name__ == "__main__":
    main()
