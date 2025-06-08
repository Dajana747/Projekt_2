"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Dajana Kočková
email: d.kockova@gmail.com
"""

import random
import time

separator = "-"*55
       
def is_numeric(number: str):
    """
    Returns True if the number contains only digits.
    """
    return number.isdigit()

def has_valid_length(number: str):
    """
    Returns True if the number has exactly 4 digits.
    """
    return len(number) == 4

def has_unique_digits(number: str):
    """
    Returns True if all digits in the number are unique.
    """
    return len(set(number)) == len(number)

def does_not_start_with_zero(number: str):
    """
    Returns True if the number does not start with zero.
    """
    return number[0] != "0"

def generate_secret_number():
    """
    Generate a random 4 digits number with only unique digits and 
    does not starts with a zero.

    Returns:
        str: 4 digits string.
    """
    while True:
        number = random.choices(range(0,10), k=4)
        generated_number = "".join(str(c) for c in number)
        if (has_unique_digits(generated_number) and 
            does_not_start_with_zero(generated_number)):
            return generated_number

def validate_input():
    """
    Validates the user's input based on defined conditions.
    If the input is invalid,the user must enter antoher guess until the guess passes all conditions.  
    """
    while True:
        guessed_number = input("Enter a number:")
        if (is_numeric(guessed_number) and
            has_valid_length(guessed_number) and
            has_unique_digits(guessed_number) and
            does_not_start_with_zero(guessed_number)):
            print(f"Your number is >>> {guessed_number}")
            return guessed_number
        else:
            print(f"Incorrect number, try again!\n{separator}")

def bulls_cows_evaluation(secret: str, guess: str):
    """
    The function creates a dictionary where the key is a digit from the generated secret number 
    and the value is a digit from the user's guess. 

    If the key is equal to the value, 1 is added to the 'bulls' counter. 
    If the key is only present among the values (but not in the same position), 
    1 is added to the 'cows' counter.

    Example:
        >>> generated_secret_number = "1234"
        >>> user_guess = "1453"
        >>> paired_digits = {'1': '1', '2': '4', '3': '5', '4': '3'}
        >>> bulls = 1
        >>> cows = 2
    """
    paired_digits = dict(zip(secret, guess))
    bulls = 0
    cows = 0
    for key, value in paired_digits.items():
        if key == value:
            bulls +=1
        elif key in paired_digits.values():
            cows +=1
    return bulls, cows

def display_bulls_cows(bulls: int, cows: int):
    """
    The function displays number of bulls and cows in a correct text form.
    """
    bull_text = f"{bulls} bull" if bulls == 1 else f"{bulls} bulls"
    cow_text = f"{cows} cow" if cows == 1 else f"{cows} cows"
    print(f"{bull_text}, {cow_text}")

if __name__ == "__main__":
    secret_number = generate_secret_number()
    attempts = 0

    print("Hi there!")
    print(separator)
    print("I've generated a random 4 digit number for you.\n"
    "Let's play a bulls and cows game.")
    print(separator)
    print("Here are some rules for you.\n"
      "The generated number:\n"
      "- Does not start with zero\n"
      "- Contains only digits (0–9)\n"
      "- Has no repeated digits")
    print(separator)

    start = time.time()

    while True:
        user_number = validate_input()
        bulls,cows = bulls_cows_evaluation(secret_number,user_number)
        display_bulls_cows(bulls,cows)
        attempts +=1
        if bulls < 4:
            (f"Number of valid attempts: {attempts}")
            print(separator)
        else:
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            print(separator)
            break

    end = time.time()
    print(f"It took you {round(end-start,2)} seconds to solve this game!\nGood job!")