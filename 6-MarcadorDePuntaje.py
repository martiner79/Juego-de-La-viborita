
#En este último apartado veremos el Marcador de puntos. También, notará algunos detalles cambiados con respecto a los anteriores.
#Ya en este punto, uds puede personalizar el juego a su gusto.

import turtle
import time
import random

#Definimos el entorno de nuestro juego.

s = turtle.Screen()
s.setup(width=600,height=600)
s.bgcolor("brown")
s.title("Proyecto La Viborita")


retraso = 0.1
Marcador = 0
Marcador_Alto = 0

#A continuación daremos algunas cualidades a nuestro personaje.

serpiente = turtle.Turtle()
serpiente.speed(0)
serpiente.shape("circle")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = 'stop'
serpiente.color("yellow")

#Creamos nuestro objeto "comida" y la lista "cuerpo"..

comida = turtle.Turtle()
comida.shape("square")
comida.color("orange")
comida.penup()
comida.goto(0,100)
comida.speed(0)

cuerpo = []

#Especifícamos los detalles del marcador, tambien llamados en ingles "score, high score".

texto = turtle.Turtle()
texto.speed()
texto.color("black")
texto.penup()
texto.goto(0, 250)
texto.write("Marcador: 0\tMarcador Alto: 0", align = "center", font = ("arial", 20, "normal"))

#Definimos los métodos de DIRECCIÓN.

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

#Definimos los atributos del MOVIMIENTO.


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

#Mandamos a "escuchar" a la consola cuando presionamos las siguientes teclas y las definimos.

s.listen()
turtle.onkeypress(arriba, "Up")
turtle.onkeypress(abajo, "Down")
turtle.onkeypress(derecha, "Right")
turtle.onkeypress(izquierda, "Left")


         
while True:

    s.update()

    #Choque de la serpiente con la pantalla.

    if serpiente.xcor() > 300 or serpiente.xcor() < -300 or serpiente.ycor() > 300 or serpiente.ycor() < -300:
        time.sleep(1)
        for i in cuerpo:
            i.hideturtle()
            i.clear()
        serpiente.home()
        serpiente.direction = 'stop'
        

        #Aquí especificamos que el marcador será 0 cuando la serpiente toque la pantalla.

        Marcador = 0
        retraso = 0.1
        texto.clear()
        texto.write("Marcador:{}\tMarcador más alto:{}".format(Marcador,Marcador_Alto), align = "center", font = ("verdana", 20, "normal"))


    #Le decimos al programa que cuando la serpiente toque la comida, esta aparezca en un punto random nuevamente.

    if serpiente.distance(comida) < 20:
        x = random.randint(-250, 250)
        y =random.randint(-250, 250)
        comida.goto(x,y)

        #Especificamos los atributos de los cuerpos que se agreguen a la serpiente.

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape("circle")
        nuevo_cuerpo.color("green")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)

        #Imprimimos por pantalla los puntajes de los Marcadores y sus detalles.

        retraso = 0.001
        Marcador += 10

        if Marcador > Marcador_Alto:
            Marcador_Alto = Marcador
        
        texto.clear()
        texto.write("Marcador:{}\tMarcador más alto:{}".format(Marcador,Marcador_Alto), align = "center", font = ("font", 20, "normal"))

    #Aquí especificamos el incremento de la serpiente a medida que vaya comiendo.

    total = len(cuerpo)
    for index in range(total -1,0,-1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x,y)

    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x,y)
       
    movimiento()

    #Le indicaremos al programa que cuando la serpiente choque con ella misma, aparezca en el lugar de origen sin el cuerpo incrementado.

    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            time.sleep(1)
            serpiente.hideturtle()
            serpiente.home()
            serpiente.showturtle()
            serpiente.direction = "stop"
            cuerpo.clear()

    #Aquí le indicamos al juego que cuando la serpiente choque con ella misma el Marcador vuelva a ser 0.
         
            Marcador = 0
            retraso = 0.1

            texto.clear()
            texto.write("Marcador:{}\tMarcador más alto:{}".format(Marcador,Marcador_Alto), align = "center", font = ("arial", 20, "normal"))

    time.sleep(retraso)

        
turtle.done()
