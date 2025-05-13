print("Question 1")
# question 1. Write a lambda function to calculate the square of a number.

calculate_square = lambda num: num * num
print(calculate_square(2))
print(calculate_square(9))


print("Question 2")
# question 2. Write a function that takes a list of numbers and returns a list containing the squares of each number using lambda.


def func(list):
    result = []
    squares = lambda input: input * input
    for input in list:
        result.append(squares(input))
    return result


print(func([1, 2, 3, 4, 5, 6, 7, 10]))


print("Question 3")
# question 3. Write a function that returns a list of prime numbers up to a given number using lambda.


def check_is_prime(number):
    check = lambda num: (number % num == 0)
    if number > 1:
        for i in range(2, number):
            if check(i):
                return False
    return True


def calc_prime(number):
    prime_list = []
    for i in range(2, number + 1):
        if check_is_prime(i):
            prime_list.append(i)
    return prime_list


print(calc_prime(7))


print("Question 4")
# question 4. Write a program that modifies a global variable inside a function.

a = 20


def update_a():
    global a
    a = a + 5
    return a


update_a()
print(a)    # 25


print("Question 5")
# question 5. Create a program that defines a function within another function and access variables from the outer function.
# (Often called Enclosing Scope)


def outer():
    print("Enter Outer")
    x = "Have a lovely day!"

    def inner():
        print("Enter Inner")
        print(x)
        print("Exit Inner")

    inner()
    print("Exit Outer")


outer()


print("Question 6")
# question 6. Create a program that defines a variable with the same name as a global variable inside a function and observe its scope.

sum = 0


def addtion(input1, input2):
    sum = input1 + input2
    return sum


print(sum)
print(addtion(5, 6))
print(sum)
