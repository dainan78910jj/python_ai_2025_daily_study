import animal


food_type = {
    "Bamboo": "vegetable",
    "Apple": "vegetable",
    "Eucalyptus leaves": "vegetable",
    "Entrecôte": "meat",
    "Kycklingfilé": "meat",
    "Lax": "meat"
}


def get_animal_list_string(animal_list):
    res = ""
    for i in range(len(animal_list)):
        res += f"{i + 1}. {animal_list[i].getName()} "
    return res.strip()


def get_food_list_string():
    res = ""
    keys = list(food_type.keys())
    for i in range(len(keys)):
        res += f"{i + 1}. {keys[i]} "
    return res.strip()


class Visitor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feed(self, animal_list):
        print(get_animal_list_string(animal_list))
        animal_index = input("Which animal you want to feed? ")
        print(get_food_list_string())
        food_index = input("What food you want to feed? ")
        keys = list(food_type.keys())
        animal_list[int(animal_index) - 1].feed(
            food_type[keys[int(food_index) - 1]])

    def wake_up(self, animal_list):
        sleeping_animals = list(filter(lambda a: a.current_state == animal.Animal_State.SLEEPING,
                                       animal_list))
        print(get_animal_list_string(sleeping_animals))
        animal_index = input("Which animal you want to wake up? ")
        sleeping_animals[int(animal_index) - 1].wake_up()

    def play(self, animal_list):
        print(get_animal_list_string(animal_list))
        animal_index = input("Which animal do you want to play with? ")
        animal_list[int(animal_index) - 1].play()
