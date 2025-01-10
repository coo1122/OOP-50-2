import random

class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} посмотрел в окно")

    def attack(self):
        print(f"{self.name} ударил правой рукой")


class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if random.random() < self.precision:
                return f"{self.name} успешно атакует врага!"
            else:
                return f"{self.name} промахивается."
        else:
            return f"{self.name} не осталось стрел!"

    def rest(self):
        self.arrows += 5
        print(f"{self.name} пополнил стрелы на 5")

    def status(self):
        print(f"Имя: {self.name}, здоровье: {self.hp}, стрелы: {self.arrows}, точность: {self.precision}")


hero1 = Archer("Ron", 100, 5, 0.7)

print(hero1.attack())
hero1.rest()
hero1.status()