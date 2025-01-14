from abc import ABC, abstractmethod
import random

class Hero(ABC):
    def __init__(self, name,lvl,hp):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.__random_int = random.randint(1,3)

    def attact(self):
        print(f"{self.name} ударил соперника рукой")

    def protection(self):
        print(f"{self.name} защитил удар соперника")

    def rest(self):
        self.hp +=5
        print(f"{self.name} пополнил здоровье на 5")

    def get_random_int(self):
        return self.__random_int
    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass
