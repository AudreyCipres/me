"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

from email import message
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """


def not_number_rejector(message):
    while True:
        try:
            user_input = int(input(message))
            print("Thank you")
            return user_input
        except Exception as e:
            print("uhh try again?")


def super_asker(low, high):
    while True:
        msg = input(f"Give me a number between {low} and {high}:")
        try:
            num = int(msg)
            if low < num < high:
                print(f"Thank you")
                return num
            else:
                print(f"{num} is not between {low} and {high}")
        except Exception as e:
            print(f"uhh could you try that again")


def advancedGuessingGame():
    print("\nWelcome to the number guessing game!")
    print("Guess a number between _ and _?")
    while True:
        try:
            lowerBound = int(input("Enter a lower bound: "))
            print("Thank you")
            break
        except ValueError:
            print("try again")
    upperBound = input(f"Enter an upper bound: ")
    while True:
        try:
            upperBound = int(input("Enter an upper bound: "))
            if lowerBound < upperBound:
                print("Thank you")
            else:
                print(f"{upperBound} is not higher than {lowerBound}")
                notAnInteger = int("a")
            break
        except ValueError:
            print(f"uhh try again?")

    print(f"OK then, a number between {lowerBound} and {upperBound} ?")

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = not_number_rejector("Guess a number:")
        print(f"You guessed {guessedNumber}")
        if guessedNumber == actualNumber:
            print(f"You got it! It was {actualNumber}")
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again")
        else:
            print("Too big, try again")
    return "wanna play again?"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
