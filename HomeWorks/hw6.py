class Footballer:
    def score(self):
        return print("Footballer score the ball")

class Left_footed(Footballer):
    def left_kick(self):
        return print("Footballer kicked the ball with left foot")

class Right_footed(Footballer):
    def right_kick(self):
        return print("Footballer kicked the ball with right foot")

class Ronaldo(Left_footed, Right_footed):
    pass

adik=Ronaldo()
adik.score()
adik.left_kick()
adik.right_kick()