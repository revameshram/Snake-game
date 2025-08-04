from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore_data.py",mode="r") as file:
             self.high_score=int(file.read())
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}        High score: {self.high_score}",False,"center",('Arial',14,'normal'))
        self.hideturtle()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score  
            with open("highscore_data.py",mode="w") as file:
             file.write(str(self.high_score))

        self.score=0
        self.update_high_score()

    def update_high_score(self): 
            self.clear()     
            self.write(f"Score: {self.score}        High score: {self.high_score}",False,"center",('Arial',14,'normal'))

    def increase(self):
        self.score+=1
        self.update_high_score()
        
    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(f"Gameover.",False,"center",('Arial',14,'normal'))
        

        
