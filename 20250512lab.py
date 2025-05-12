# question 1, Given a list of integers, return True if the sequence of number 1,2,3 appears in the list somewhere.

print('Question 1')
list1 = [1, 1, 2, 3, 1]
list2 = [1, 1, 2, 4, 1]
list3 = [1, 1, 2, 1, 2, 3]


def sequence_123_check(list):
    if (len(list) < 3):
        return False
    else:
        for i in range(len(list) - 2):
            if (list[i] == 1) and (list[i + 1] == 2) and (list[i + 2] == 3):
                return True
        return False


print(sequence_123_check(list1))
print(sequence_123_check(list2))
print(sequence_123_check(list3))

# question 2, Given a string, return a new string made of every other character staring with the first, so "Hello" yields "Hlo".

print('Question 2')


def string_bits(string):
    new_string = ""
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i]
    return new_string


print(string_bits("Heeololeo"))
print(string_bits("AaBbCcDd"))


# question 3, Given a string, return a string where for every char in the original, there are two chars.

print('Question 3')


def double_character(string):
    result = ""
    for i in string:
        # result += i + i
        result += i * 2
    return result


res = double_character("have-a-good-day")
print(res)


# question 4, Return the number of even integers in the given array/list.

print('Question 4')


def count_evens(list):
    get_sum = 0
    for item in list:
        if item % 2 == 0:
            get_sum += 1
    return get_sum


res = count_evens([0, 1, 4, 7, 8, 12, 110])
print(res)


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
