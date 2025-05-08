# question 1, Write a program that takes two integers as input, base and exponent, and calculates the power using loops.
input_base = input("Please enter a integer number as base: ")
input_exponent = input("Please enter a integer number as exponent: ")

base_int = int(input_base)
result = 1
for i in range(int(input_exponent)):
    result *= base_int
print(result)


# question 2, Write a program that calculates the sum of all elements in a given tuple.
my_tup = (1, 5, 7, 25, 48, 97, 90.5)

get_sum = 0
for item in my_tup:
    get_sum += item
print(get_sum)
# output is 273.5


# question 3, Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.
given_tup = (3, 17, 22, 58, 60, 99, 204, 662, 878, 999)
new_list = []
for item in given_tup:
    if item % 2 == 0:
        new_list.append(item)

new_tup = tuple(new_list)
print(new_tup)


# question 4, Write a program that merges two dictionaries into a single dictionary.
# If a key is common to both dictionaries, the value from the second dictionary should be used.

studentsname_in_dic1 = {
    1: "Linda",
    2: "Sara",
    3: "Kevin",
    4: "Bruno"
}

studentsname_in_dic2 = {
    4: "Anna",
    5: "Christina",
    6: "Eleonora"
}
studentsname_in_dic1.update(studentsname_in_dic2)
print(studentsname_in_dic1)


# question 5, Write a program that takes a list of integers as input
# and uses list comprehension to create a new list containing only the even numbers from the original list.
given_list = [6, 35, 41, 46, 53, 69, 77, 82, 94, 112, 139, 159, 200]

get_even_number = [item for item in given_list if item % 2 == 0]

print(get_even_number)
# output is [6, 46, 82, 94, 112, 200]


# question 6, Write a program that takes a string as input and prints its reverse.
input_str = input("Please enter a string: ")
reversed_str = input_str[::-1]
print(reversed_str)

# question 7, You are given a list called mypairs. This list contains several tuples, and each tuple holds exactly 10 integers.
# Your task is to write two different solutions that print out each individual value inside the tuples:
# Manual unpacking – Do it like we did in class: unpack all 10 values into individual variables in the for-loop.
# Smarter unpacking – Write an alternative solution that achieves the same result, but in a more flexible or elegant way
# (e.g. a solution that would still work if the number of values changes in the future).

mypairs = [(3, 14, 56, 78, 99, 118, 165, 158, 164, 190),
           (1, 3, 5, 7, 9, 11, 13, 15, 17, 20),
           (2, 4, 6, 8, 10, 12, 14, 16, 18, 19)]

# Manual unpacking
for i0, i1, i2, i3, i4, i5, i6, i7, i8, i9 in mypairs:
    print(i0, i1, i2, i3, i4, i5, i6, i7, i8, i9)


# Smarter unpacking
mypairs = [(3, 14, 56, 78, 99, 118, 165, 158, 164, 190),
           (1, 3, 5, 7, 9, 11, 13, 15, 17, 20),
           (2, 4, 6, 8, 10, 12, 14, 16, 18, 19)]

for item in mypairs:
    for j in item:
        print(j)
