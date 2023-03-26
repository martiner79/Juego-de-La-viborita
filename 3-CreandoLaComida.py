
import turtle
import time
import random

retraso = 0.1

#Definimos el entorno de nuestro juego

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("gray")
s.title("Segundo Proyecto")

#A continuación daremos algunas cualidades a nuestro personaje

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = 'stop'
serpiente.color("green")

#Creamos nuestro objeto "Comida" y sus cualidades

comida = turtle.Turtle()
comida.shape("circle")
comida.color("orange")
comida.penup()
comida.goto(0,100)
comida.speed(0)


def arriba():
    if serpiente.direction != "down":
        serpiente.direction = "up"

def abajo():
    if serpiente.direction != "up":
        serpiente.direction = "down"

def izquierda():
    if serpiente.direction != "right":
        serpiente.direction = "left"

def derecha():
    if serpiente.direction != "left":
        serpiente.direction = "right"



def movimiento():
    if serpiente.direction == 'up':
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    if serpiente.direction == 'down':
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    if serpiente.direction == 'right':
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    if serpiente.direction == 'left':
        x = serpiente.xcor()
        serpiente.setx(x - 20)

s.listen()
turtle.onkeypress(arriba, "Up")
turtle.onkeypress(abajo, "Down")
turtle.onkeypress(derecha, "Right")
turtle.onkeypress(izquierda, "Left")


while True:
    s.update()
    if serpiente.distance(comida) < 20:
        x = random.randint(-250, 250)
        y =random.randint(-250, 250)
        comida.goto(x,y)
    

    movimiento()
    time.sleep(retraso)

        

turtle.done()
