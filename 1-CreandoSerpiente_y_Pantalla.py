

import turtle
import time
retraso = 0.1

#Definimos el entorno de nuestro juego.

s = turtle.Screen()
s.setup(650,650)    #Tamaño de la pantalla.
s.bgcolor("gray")
s.title("Proyecto la Viborita")

#A continuación daremos algunas cualidades a nuestro personaje.

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape("circle")  #Cabeza de la serpiente. En el caso de querer un círculo, simplemente colocamos "circle".
serpiente.penup()  #Esto lo colocamos para que la serpieten no "dibuje" una línea a medida que avanza.
serpiente.goto(0,0)
serpiente.direction = 'stop'  #Cuando se ejecute el programa, o termine, la serpiente empieza desde la dirección X=0, Y=0 y con "stop" para no moverse.
serpiente.color("orange")


turtle.done()
