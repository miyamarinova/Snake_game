from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My SNake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
not_eaten = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.update_score()

    #Detect collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.increased_score()

    #Detect collision with wall.
    if int(snake.head.xcor()) > 280 or int(snake.head.xcor()) < -280 or int(snake.head.ycor()) > 280 or int(snake.head.ycor()) < -280:
        game_is_on = False
        score.game_over()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()




                                            #if the snake's head is 15 pixels -> collision
                                      # => snake eat the food, so we need new foo
screen.exitonclick()
