import aquatic
import carnivore
import animal


class Dolphin(aquatic.Aquatic, carnivore.Carnivore):
    def __init__(self):
        super().__init__()
        self.energy_low_threshold = -1


# dolphin_instance = Dolphin()
# dolphin_instance.wake_up()
