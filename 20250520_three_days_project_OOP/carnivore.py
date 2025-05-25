import animal


class Carnivore(animal.Animal):
    def __init__(self):
        super().__init__()

    def feed(self, food_type):
        if food_type == "meat":
            result = super().eat()
            if result:
                print("I am eating.")
            else:
                print("I do not want to eat.")
        else:
            print("This is not my food type :(")


# c_tiger = Carnivore()
# c_tiger.satiety = 6
# c_tiger.feed("meat")
# c_tiger.feed("apple")
