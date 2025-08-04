from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed(0)
        food_x=random.randint(-280,280)
        food_y=random.randint(-280,280)
        self.goto(food_x,food_y)

    def new_food(self):    
        food_x=random.randint(-280,280)
        food_y=random.randint(-280,280)
        self.goto(food_x,food_y)

