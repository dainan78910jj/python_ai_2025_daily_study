# question 1. Veichle Inheritance
# Create a Python program that models a hierarchy of vehicles using inheritance.
# Start with a base class Vehicle, and then create two or more derived classes (e.g., Car,Bicycle, Motorcycle) that inherit from the Vehicle class.
# Each class should have specific attributes and methods related to the type of vehicle it represents.

# 1. Define the Vehicle base class with common attributes such as make, model, and year, and methods like start(), stop(), and fuel_up()
# 2. Create derived classes for different types of vehicles, e.g., Car, Bicycle, and Motorcycle. Each derived class should inherit from the Vehicle base class and add attributes and methods specific to that type of vehicle. For example, the Car class might have attributes like num doors, and the Bicycle class could have attributes like num gears
# 3. Implement specific methods for each derived class. For instance, the Car class might have a method to honk the horn, and the Bicycle class could have a method to ring the bell.
# 4. Create instances of each vehicle type and demonstrate their specific methods and attributes. For example, you can create a car, bicycle, and motorcycle, and call methods like start(), stop(), and their specific methods like honk_horn() or ring bell()

class Vehicle:

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.is_running = False
        self.fuel_level = 0

    def start(self):
        if self.fuel_level > 20:
            self.is_running = True
        return self.is_running

    def stop(self):
        self.is_running = False
        return self.is_running

    def fuel_up(self):
        self.fuel_level = 100


class Car(Vehicle):

    def __init__(self, model, year, number_of_passenger):
        super().__init__(model, year)
        self.number_of_passenger = number_of_passenger
        self.current_number_of_persons = 0

    def __str__(self):
        return f"This is a {self.model} car of year {self.year} and having {self.number_of_passenger} seats. Currently is{'' if self.is_running else ' not'} running, {self.current_number_of_persons} on board."

    def on_board(self, number_of_person):
        if self.current_number_of_persons + number_of_person > self.number_of_passenger or self.is_running == True:
            return False
        else:
            self.current_number_of_persons += number_of_person
            return True


class Motorcycle(Vehicle):
    def __init__(self, model, year, wheel_distance):
        super().__init__(model, year)
        self.wheel_distance = wheel_distance

    def get_wheel_distance(self):
        return self.wheel_distance


car_instance = Car("BMW 330", 2015, 5)
print(car_instance)
car_instance.on_board(1)
print(car_instance)
car_instance.start()
print(car_instance)
car_instance.fuel_up()
car_instance.start()
print(car_instance)
car_instance.on_board(2)
print(car_instance)

motorcycle_instance = Motorcycle("GSX1300R", 2000, 1485)
print(motorcycle_instance.get_wheel_distance())

# question 2. Multiple Inheritance and MRO Challenge

# Task:
# 1. Create classes X, Y,Z, each with an identify() method
# 2.Create a class W that inherits from both X and Y
# 3.Call the identify() method on an instance of W and print the MRO of W
#
# Challenge:
# 4. Add a super() call in one of the subclasses identify() methods to observe how method chaining works.


class X:
    def __init__(self):
        pass

    def identify(self):
        print("x")


class Y:
    def __init__(self):
        pass

    def identify(self):
        print("y")


class Z(Y, X):
    def __init__(self):
        pass

    def identify(self):
        super().identify()
        super(Y, self).identify()
        print("z")


class W(X, Y):
    pass


w = W()
w.identify()
print(W.mro())

z = Z()
z.identify()
print(Z.mro())
