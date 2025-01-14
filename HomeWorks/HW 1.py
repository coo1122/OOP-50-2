class Hero:
    def __init__(self,name,lvl,hp):
        self.name=name
        self.hp=hp
        self.lvl=lvl

    def introduce(self):
        print(f'Привет, меня зовут {self.name}, мой lvl {self.lvl} , мое HP {self.hp}')

    def is_adult(self):
        return self.lvl>=10

    def __str__(self):
        return (f"Имя:{self.name}, lvl: {self.lvl}, HP: {self.hp}")

hero_1=Hero(name='Jack',lvl=57,hp=1000)
hero_2=Hero(name='Ron',lvl=3,hp=1000)
hero_3=Hero(name='Cole',lvl=10,hp=1000)
hero_1.introduce()

print(hero_1.is_adult())
print(hero_2.is_adult())
print(hero_3.is_adult())

print(hero_2)