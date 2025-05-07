# 1, Given the string
s = "Python"
print(s[4])
print(s[-2])
# output: o


print(s[0:4])
print(s[:4])
print(s[:-2])
# output: Pyth


print(s[1:4])
print(s[:4][1:])
print(s[1:][:-2])
# output: yth


print(s[::-1])
# output: nohtyP


# 2, Given the nested list
l = [3, 7, [1, 4, "hello"]]

l[2][2] = "goodbye"
print(l)
# reassign "hello" to "goodbye"


# 3, Using keys and indexing, grab the "hello" from the fllowing dictionaries
d1 = {
    "simple_key": "hello"
}

print(d1["simple_key"])


d2 = {
    "k1": {
        "k2": "hello"
    }
}

print(d2["k1"]["k2"])


d3 = {
    "k1": [
        {
            "nest_key": [
                "this is deep",
                ["hello"]
            ]
        }
    ]
}

print(d3["k1"][0]["nest_key"][1][0])


# 4, Use a set to find the unique values of the list below:
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
print(set(mylist))


# 5, You are given two variables:
age = 4
name = "Sammy"

print(f"Hello my dog's name is {name} and he is {age} years old.")
print("Hello my dog's name is {n} and he is {a} years old.".format(
    n=name, a=age))
