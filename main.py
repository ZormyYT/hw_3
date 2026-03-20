import time
import random


class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def eat(self):
        print(f"{self.name} їсть...")
        self.hunger -= 20
        self.energy += 5
        time.sleep(2)

    def sleep(self):
        print(f"{self.name} спить...")
        self.energy += 30
        self.hunger += 10
        time.sleep(3)

    def play(self):
        print(f"{self.name} грається...")
        self.happiness += 20
        self.energy -= 15
        self.hunger += 10
        time.sleep(2)

    def status(self):
        print(f"\nСтан {self.name}:")
        print(f"Голод: {self.hunger}")
        print(f"Енергія: {self.energy}")
        print(f"Настрій: {self.happiness}\n")

    def live(self):
        actions = [self.eat, self.sleep, self.play]

        while True:
            self.status()

            if self.hunger >= 80:
                print(f"{self.name} дуже голодний!")
                self.eat()

            elif self.energy <= 20:
                print(f"{self.name} втомився!")
                self.sleep()

            else:
                action = random.choice(actions)
                action()

            self.hunger += 5
            self.energy -= 5
            self.happiness -= 3

            # if self.hunger < 0:
            #     self.hunger = 0
            # elif self.hunger > 100:
            #     self.hunger = 100

            self.hunger = min(max(self.hunger, 0), 100)
            self.energy = min(max(self.energy, 0), 100)
            self.happiness = min(max(self.happiness, 0), 100)

            if self.hunger >= 100:
                print(f"{self.name} помер від голоду...")
                break

            if self.happiness <= 0:
                print(f"{self.name} дуже сумний...")
                break

            time.sleep(2)

name = input("Введіть ім'я тваринки: ")

pet = Pet(name)
print(f"\nВаш {name} починає життя!\n")

pet.live()