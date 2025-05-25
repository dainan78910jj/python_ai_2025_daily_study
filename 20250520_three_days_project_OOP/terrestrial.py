import animal


class Terrestrial(animal.Animal):
    def __init__(self):
        super().__init__()

    def play(self):
        result = super().play()
        if result:
            print("I am playing.")
        else:
            print("I do not want to play.")


# t_tiger = Terrestrial()
# t_tiger.play()
