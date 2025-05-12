# question 5, optional lab
# Make a simple command line game. You could put together everything you have learned so far abbout Python.
# The game goes like this:
# step 1: the computer will think of 3 digit number that has no repeating digits.
# step 2: you will then guess a 3 digit number
# step 3: the computer will then give back clues, the possible clues are:
# Close: you have guessed a correct number but in the wrong position
# Match: you have guessed a correct number in the correct position
# Nope: you have not guess any of the numbers correctly
# step 4: based on these clues you will guess again until you break the code with a perfect match!

import random


def add_number_to_list(list, new_number):
    for n in list:
        if n == new_number:
            return False

    list.append(new_number)
    return True


def create_list():
    list = []
    while len(list) < 3:
        add_number_to_list(list, random.randint(1, 10))

    return list


def input_list():
    list = []
    while len(list) < 3:
        new_input = int(input("Please give a new number: "))
        if not add_number_to_list(list, new_input):
            print(f"The given number {new_input} is already added.")

    return list


def compare(c_list, g_list):
    if c_list[0] == g_list[0] and c_list[1] == g_list[1] and c_list[2] == g_list[2]:
        return "Perfect Match"

    if c_list[0] == g_list[0] or c_list[1] == g_list[1] or c_list[2] == g_list[2]:
        return "Match"

    for i in c_list:
        for j in g_list:
            if i == j:
                return "Close"

    return "None"


def main():
    computer_list = create_list()

    guess_list = input_list()
    res = compare(computer_list, guess_list)

    while res != "Perfect Match":
        print(res)
        guess_list = input_list()
        res = compare(computer_list, guess_list)

    print("Congratulations!")
    print(computer_list)


main()
