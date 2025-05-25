from threading import Timer
import koala
import panda
import dolphin
import grass_carp
import visitor

zoo_animal_list = [koala.Koala(), panda.Panda(
), dolphin.Dolphin(), grass_carp.GrassCarp()]

zoo_animal_list[1].name = "盼盼"


def timer():
    for animal in zoo_animal_list:
        animal.tick()
    t = Timer(1, timer)
    t.start()


timer()

while True:
    name = input("Welcome to the zoo, what is your name? ")
    age = input("How old are you? ")
    current_visitor = visitor.Visitor(name, int(age))
    print(f"Hi {current_visitor.name}!")
    while True:
        activity = input(
            "What do you want to do? (1. feed animal 2. wake up animal 3. play with animal 0. leave the zoo)\n")
        if activity == "1":
            current_visitor.feed(zoo_animal_list)
        elif activity == "2":
            current_visitor.wake_up(zoo_animal_list)
        elif activity == "3":
            current_visitor.play(zoo_animal_list)
        elif activity == "0":
            print(f"Goodbye {current_visitor.name}!")
            break
        else:
            print("Invalid choice")
