from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.h_score = 0
        with open("data.txt") as data:
            self.h_score = int(data.read())
        self.color('red')
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, Highest Score: {self.h_score}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.h_score:
            self.h_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.h_score}")
        self.score = 0
        self.update_scoreboard()




