import math

# Exercise 1 Polymorphism
# Create a Python program that explores polymorphism using a hierarchy of shapes.
# Start with a base class Shape, and then create two or more derived classes(e.g., Circle, Rectangle, Triangle) that inherit from the Shape class.
# Each shape class should have its own implementation of methods like area() and perimeter(). These methods will calculate the area and perimeter of the respective shape.

# 1. Define the Shape base class with methods like area() and perimeter(). You can initialize any common attributes in the base class .

# 2. Create derived classes for different shapes, e.g., Circle, Rectangle, and Triangle. Each derived class should inherit from the Shape base class and implement its own version of the area() and perimeter() methods.

# 3. Implement specific methods for each derived class . For example, the Circle class might have a method to calculate its area based on the radius,
#    and the Rectangle class could have a method to calculate its area based on length and width.
#
#    Create instances of each shape type and demonstrate the use of polymorphism by calling the area() and perimeter() methods on them.
print("Exercise 1 Polymorphism")


class Geometry:
    def __init__(self):
        pass

    def perimeter(self):
        pass

    def area(self):
        pass


class Rectangle(Geometry):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width


class Circle(Geometry):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius * self.radius


class Triangle(Geometry):
    def __init__(self, length1, length2, length3):
        super().__init__()
        self.length1 = length1
        self.length2 = length2
        self.length3 = length3

    def perimeter(self):
        return self.length1 + self.length2 + self.length3

    def area(self):
        s = (self.length1 + self.length2 + self.length3) / 2
        a_sq = s * (s - self.length1) * (s - self.length2) * (s - self.length3)
        return math.sqrt(a_sq)


r_instance = Rectangle(10, 7)
c_instance = Circle(10)
t_instance = Triangle(3, 4, 5)

print(r_instance.perimeter())
print(c_instance.perimeter())
print(t_instance.perimeter())

print(r_instance.area())
print(c_instance.area())
print(t_instance.area())


# Exercise 2 Implement a Plugin System Using Duck Typing
# Create classes UpperCaseFormatter, LowerCaseFormatter, and TitleCaseFormatter that implement a format_text(text) method.
# Write a function apply_formatters(text, formatters) that applies a list of formatters to a string.
#

# Bonus:
# Add error handling to check if objects passed to apply_formatters actually have a format_text() method, raising a custom FormatterError if not.

print("Exercise 2 Implement a Plugin System Using Duck Typing")


class UpperCaseFormatter:
    def __init__(self):
        pass

    def format_text(self, input):
        return input.upper()


class LowerCaseFormatter:
    def __init__(self):
        pass

    def format_text(self, input):
        return input.lower()


class TitleCaseFormatter:
    def __init__(self):
        pass

    def format_text(self, input):
        return input.title()


class ExceptionFormatter:
    def __init__(self):
        pass

    def format_string(self, input):
        return input


class FormatterError(Exception):
    pass


def apply_formatters(formatter, input):
    if hasattr(formatter, 'format_text') and callable(formatter.format_text):
        return formatter.format_text(input)
    else:
        raise FormatterError(
            "Formatter does not have method called format_text()")


formatter_list = [UpperCaseFormatter(), LowerCaseFormatter(),
                  TitleCaseFormatter(), ExceptionFormatter()]

for formatter in formatter_list:
    try:
        print(apply_formatters(formatter, 'Hello world!'))
    except Exception:
        print(f"Exception: {Exception}")
