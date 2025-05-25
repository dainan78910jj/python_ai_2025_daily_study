import terrestrial
import herbivore
import animal

# 陆地 食草动物


class Koala(terrestrial.Terrestrial, herbivore.Herbivore):
    def __init__(self):
        super().__init__()
        self.energy_low_threshold = 8

    def wake_up(self):
        if self.current_state == animal.Animal_State.SLEEPING:
            if self.energy < 6:
                print("I am still sleepy. Do not bother me.")
            else:
                super().wake_up()
                print("What happen?")
        else:
            print("I am not sleeping.")


# koala_instance = Koala()
# koala_instance.wake_up()
# koala_instance.current_state = animal.Animal_State.SLEEPING
# koala_instance.wake_up()

# koala_instance.tick()
# koala_instance.tick()
# koala_instance.tick()
# koala_instance.tick()
# koala_instance.wake_up()


# koala_instance.feed("meat")
# koala_instance.play()
