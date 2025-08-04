from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(600,600)
screen.tracer(0)

snake=Snake()
food=Food()
scores=Scoreboard()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")

is_on=True

while is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

#check food collision:
    if snake.head.distance(food)<15:
        food.new_food()
        snake.extend()
        scores.increase()        

#check wall collision:

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290 or snake.head.ycor()>290 :
        scores.reset()
        snake.reset_snake()
        

#check tail collision:
    
    for segments in snake.full_snake[3:]:#slicing the list
        if snake.head.distance(segments)<10:
            scores.reset()
            snake.reset_snake()
            

    
screen.exitonclick()

