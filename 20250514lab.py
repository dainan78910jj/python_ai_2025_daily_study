class Student:

    # question 1. Define a Student Class:
    # Define a class named Student with the following attributes:
    # - name: Name of the student (string).
    # - age: Age of the student (int).
    # - grade: Grade level of the student (int).

    def __init__(self, name="", age=7, grade=1):
        self.name = name
        self.age = age
        self.grade = grade


# question 2. Add Methods:
# Add the following methods to the Student class:
# - get_info( ): Method to display the student's information.
# - promote ( ): Method to promote the student to the next grade level.


    def get_info(self):
        print(
            f"{self.name} is {self.age} yesrs old and in grade {self.grade}.")

    def promote(self):
        self.grade = self.grade + 1
        return self.grade


# question 3. Test the Class:
# Create instances of the Student class and test its methods:
# - Create a student named "Anna" with age 15 and grade 9. Use the get_info() method to display her information.
# - Promote Anna to the next grade level using the promote() method, then use get_info() to display her updated information.


print("Question 3")

anna_instance = Student("Anna", 15, 9)
anna_instance.get_info()
anna_instance.promote()
anna_instance.get_info()


# queston 4. convert the following code int list comprehension
# class Something:
#     def __init__(self, data:dict):
#         self.__dict__ = data

#     def __str__(self):
#         str_rep = ''
#         for key, value in self.__dict__.items():
#             str_rep += f'{key} = {value}'
#         return str_rep

print("Question 4")

data_dict1 = {
    'a': 10,
    'b': 20,
    'name': 'One'
}

data_dict2 = {
    'c': 15,
    'd': 25,
}


class Something:
    def __init__(self, data: dict):
        self.__dict__ = data

    def __str__(self):
        list = [f'{key} = {value} ' for key,
                value in self.__dict__.items()]
        str_rep = ''.join(list)
        str_rep = str_rep.strip()
        return str_rep


s1 = Something(data_dict1)
s2 = Something(data_dict2)
print(s1)
print(s2)
