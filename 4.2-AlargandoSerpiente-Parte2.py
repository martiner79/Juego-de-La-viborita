
import turtle
import time
import random

retraso = 0.1

#Definimos el entorno de nuestro juego.

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("gray")
s.title("Segundo Proyecto")

#A continuación daremos algunas cualidades a nuestro personaje.

serpiente = turtle.Turtle()
serpiente.speed(2)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = 'stop'
serpiente.color("green")

#Creamos nuestro objeto "comida" y sus cualidades.

comida = turtle.Turtle()
comida.shape("circle")
comida.color("orange")
comida.penup()
comida.goto(0,100)
comida.speed(0)

cuerpo = []

#Definimos los métodos de DIRECCIÓN .

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

    

    if serpiente.distance(comida) < 20:
        x = random.randint(-250, 250)
        y =random.randint(-250, 250)
        comida.goto(x,y)


        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("green")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)

    total = len(cuerpo)                     
    for index in range(total -1,0,-1):     #Con el primer -1 le indicamos que queremos que se agregue un cuerpo (un valor a lista) y se agreguen
        x = cuerpo[index-1].xcor()         #valores por detrás de la cabeza de la serpiente. Con el cero 0 indicamos que esa parte no se
        y = cuerpo[index-1].ycor()         #debe contar, ya que representa la cabeza. Y el -1 al final, indica la cantidad de valores que 
        cuerpo[index].goto(x,y)            #que se agregarán. En este caso irá de uno en uno (hacia atrás) a media que la serpiente coma.

    if total > 0:
        x = serpiente.xcor()               #Con las coordenadas (x,y) e [index-1] nos referimos a la ubicación donde se colocará el nuevo
        y = serpiente.ycor()               #cuerpo. Es decir, una dirección por detrás (-1) del último en la lista.
        cuerpo[0].goto(x,y)                #Al final, a través de total > 0 iremos sumando las partes del cuerpo a medida que la serpiente coma.

    movimiento()

    

    time.sleep(retraso)

        

turtle.done()
