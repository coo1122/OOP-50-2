from main import Hero

class Jester(Hero):

    def unique_attack(self):
        print(f"{self.name} совершил серию ударов рукой")

    def unique_scream(self):
        print(f"{self.name} крикнул на соперника")

    def action(self):
        random_int=self.get_random_int()
        if random_int==1:
            self.attact()
        elif random_int==2:
            self.protection()
        elif random_int==3:
            self.rest()


adik=Jester("adik",100,100)
adik.unique_attack()
adik.unique_scream()
adik.action()