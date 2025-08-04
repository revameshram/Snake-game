from turtle import Turtle

POSITIONS=[(0, 0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:
    def __init__(self):
        self.full_snake=[]
        self.create_snake()
        self.head=self.full_snake[0]
        

    def add_segment(self,position):
        snake=Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.full_snake.append(snake)

    def create_snake(self):    
        for position in POSITIONS:
            self.add_segment(position)


    def extend(self):
        self.add_segment(self.full_snake[-1].position())

    def reset_snake(self):
        for seg in self.full_snake:
            seg.goto(1000,1000)
        self.full_snake.clear()
        self.create_snake()
        self.head=self.full_snake[0]

    def move(self):
        
        for snake in range(len(self.full_snake)-1,0,-1):
            new_x=self.full_snake[snake-1].xcor()
            new_y=self.full_snake[snake-1].ycor()
            self.full_snake[snake].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

        