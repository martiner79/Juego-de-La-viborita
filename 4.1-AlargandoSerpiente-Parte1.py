
import turtle
import time
import random

retraso = 0.1

#Definimos el entorno de nuestro juego

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("gray")
s.title("Proyecto La Viborita")

#A continuación daremos algunas cualidades a nuestro personaje

serpiente = turtle.Turtle()
serpiente.speed(0)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = 'stop'
serpiente.color("green")

#Creamos nuestro objeto "comida" y sus cualidades

comida = turtle.Turtle()
comida.shape("circle")
comida.color("orange")
comida.penup()
comida.goto(0,100)
comida.speed(0)

#Creamos una lista vacía donde almacenaremos el nuevo cuerpo de la serpiente

cuerpo = []


#Direcciones

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


#Movimientos

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


#Teclas que le darán la acción de movimiento a nuestra serpiente (flechitas)

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

    nuevo_cuerpo = turtle.Turtle()          #Creamos las cualidades del nuevo cuerpo de la serpiete. Si ejecutamos este programa hasta aquí
    nuevo_cuerpo.shape("square")            #veremos que el nuevo cuerpo aparece en las coordenas (0,0) cada vez que la serpiente come.
    nuevo_cuerpo.color("orange")            #Por lo tanto, en el siguiente apartado veremos las funciones para configurar y agregar a la lista.
    nuevo_cuerpo.penup()
    nuevo_cuerpo.goto(0,0)
    nuevo_cuerpo.speed(0)

    movimiento()
    time.sleep(retraso)

        

turtle.done()
