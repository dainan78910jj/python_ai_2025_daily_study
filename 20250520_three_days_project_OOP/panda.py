import terrestrial
import carnivore
import herbivore

# 陆地 食肉 食草动物


class Panda(terrestrial.Terrestrial, herbivore.Herbivore, carnivore.Carnivore):
    def __init__(self):
        super().__init__()

    def feed(self, food_type):
        if food_type == "vegetable":
            super().feed(food_type)
        else:
            # skip herbivores feed method, call carnivores feed method
            super(herbivore.Herbivore, self).feed(food_type)

    def wake_up(self):
        super().wake_up()
        print("")


# panda_instance = Panda()

# panda_instance.feed("vegetable")
# panda_instance.feed("meat")
