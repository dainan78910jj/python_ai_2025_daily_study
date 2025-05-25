import animal


class Herbivore(animal.Animal):
    def __init__(self):
        super().__init__()

    def feed(self, food_type):
        if food_type == "vegetable":
            result = super().eat()
            if result:
                print("I am eating vegetables.")
            else:
                print("I am not hungry.")
        else:
            print("I am vegetarin. This is not my food type.")


# h_horse = Herbivore()
# h_horse.satiety = 7
# h_horse.feed("vegetable")
# h_horse.feed("meat")
