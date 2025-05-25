import animal


class Aquatic(animal.Animal):
    def __init__(self):
        super().__init__()

    def play(self):
        result = super().play()
        if result:
            print("I am playing in the water.")
        else:
            print("I do not want to play in the water.")


# a_fish = Aquatic()
# a_fish.play()
