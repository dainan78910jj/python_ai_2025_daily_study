import aquatic
import herbivore
import animal


class GrassCarp(aquatic.Aquatic, herbivore.Herbivore):
    def __init__(self):
        super().__init__()
        self.energy_low_threshold = 2

    def wake_up(self):
        if self.current_state == animal.Animal_State.SLEEPING:
            if self.energy > 3:
                super().wake_up()
                print("Hello!")
            else:
                print("I am still sleepy. I need one more hour.")
        else:
            print("I am not sleeping")


# gc_instance = GrassCarp()
# gc_instance.wake_up()
