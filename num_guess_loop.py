#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Jan. 11, 2022
# This program asks the user to guess a number between
# 0 and 9 and then uses a loop to check if the guessed number 
# is equal to the random number generated

import random

def main():
    # initialize the loop counter and the random number
    loop_counter = 0
    # generate random number
    random_number = random.randint(0, 9)
    
    while True:
        # get the guessed number as string
        guessed_number_string = input("Guess a number between 0 and 9: ")
        try:
            # checks for errors
            guessed_number = int(guessed_number_string)
            # check to see if the guessed number is in the range 0 and 9
            if guessed_number >= 0 and guessed_number <= 9:
                loop_counter = loop_counter + 1
                if guessed_number == random_number:
                    # Display the result
                    print("")
                    print("Your guess is correct. Thanks for playing.")
                    break
                else:
                    #Display the result
                    print("Your guess is wrong. The correct number is {}".format(random_number))
                    print("")
                    print("Tracking {} times through the loop.".format(loop_counter))
                    print("")
            else:
                print("{} is not in the range of numbers to guess from. Please try again.".format(guessed_number))
        except Exception:
            print("{} is not a number. Please try again.".format(guessed_number_string))


if __name__ == "__main__":
      main()