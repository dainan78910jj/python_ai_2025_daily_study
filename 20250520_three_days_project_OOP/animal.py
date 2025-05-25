# Develop a Simulation System for a Zoo
from enum import Enum


class Animal_State(Enum):
    AWAKE = 0
    EATING = 1
    SLEEPING = 2
    HUNTING = 3
    PLAYING = 4


class Animal:
    def __init__(self):
        self.energy = 5
        self.satiety = 5
        self.current_state = Animal_State.AWAKE
        self.energy_low_threshold = 3
        self.name = ""

    def getName(self):
        if len(self.name) == 0:
            return type(self).__name__
        else:
            return f"{self.name}({type(self).__name__})"

    def tick(self):
        if self.satiety == 0 and self.energy == 0:
            # print(f"{self.getName()} dead.")
            return

        elif self.satiety < 3:
            if self.current_state != Animal_State.HUNTING and self.current_state != Animal_State.EATING:
                self.current_state = Animal_State.HUNTING
                # print(f"{self.getName()} is hungry, looking for food.")

        elif self.energy < self.energy_low_threshold and self.current_state != Animal_State.SLEEPING:
            self.current_state = Animal_State.SLEEPING
            # print(f"{self.getName()} go to sleep.")

        match self.current_state:
            case Animal_State.AWAKE:
                self.energy -= 0.5
                self.satiety -= 0.5

            case Animal_State.EATING:
                if self.satiety < 10:
                    self.satiety += 5
                else:
                    self.current_state = Animal_State.AWAKE
                    # print(f"{self.getName()} stop eating.")
                self.energy -= 0.5

            case Animal_State.SLEEPING:
                if self.energy < 10:
                    self.energy += 1
                else:
                    self.current_state = Animal_State.AWAKE
                    # print(f"{self.getName()} wake up.")
                self.satiety -= 0.5

            case Animal_State.HUNTING:
                self.current_state = Animal_State.EATING
                # print(f"{self.getName()} start eating.")

            case Animal_State.PLAYING:
                self.energy -= 2
                self.satiety -= 1

    def eat(self):
        if self.current_state != Animal_State.SLEEPING and self.satiety < 8:
            self.current_state = Animal_State.EATING
            # print(f"{self.getName()} start eating.")
            return True
        else:
            return False

    def wake_up(self):
        if self.current_state == Animal_State.SLEEPING:
            self.current_state = Animal_State.AWAKE
            print(f"{self.getName()} wake up.")

    def play(self):
        if self.current_state == Animal_State.AWAKE:
            self.current_state = Animal_State.PLAYING
            # print(f"{self.getName()} start playing.")
            return True
        else:
            return False
