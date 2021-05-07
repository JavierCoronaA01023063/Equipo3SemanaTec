
"""Snake, classic arcade game.
Aranza Balleza A01023871
Snake, classic arcade game.

Exercises
1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.
"""

from turtle import *
from random import randrange
from freegames import square, vector

import turtle

food = vector(0, 0)
snake = [vector(-170, 170)]   #Cambio de números empezar desde la esquina superior izquierda
aim = vector(0, -10)

#Agregarle un titulo al prograrma
turtle.title("My Snake Program")
#Cambia el color y contorno de la flecha 
t.color("blue", "red")

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:

        square(body.x, body.y, 9, 'green')   #Se le cambió el color a la serpiente de negro a verde

    square(food.x, food.y, 9, 'yellow')    # Se cambió el color de la comida a amarillo también
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()