
import turtle
import time
import random

retraso = 0.1

#Definimos el entorno de nuestro juego.

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("gray")
s.title("Proyecto La Viborita")

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

#Definimos los atributos del Movimiento.


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

    #Definimos las colisiones con los bordes de la pantalla.

    if serpiente.xcor() > 300 or serpiente.xcor() < -300 or serpiente.ycor() > 300 or serpiente.ycor() < -300:
        time.sleep(1)
        for i in cuerpo:        #Después de tocar la pantalla, lo primero que ocurrirá será un "clear", es decir, eliminar los cuerpos 
            i.hideturtle()      #agregados. Luego, con "hideturtle" hacemos "invisible" el cuerpo. Y finalmente aparece en (0,0)
            i.clear()
        serpiente.home()
        serpiente.direction = 'stop'
        

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
    for index in range(total -1,0,-1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x,y)

    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x,y)
       
    movimiento()                            #Definimos las colisiones con el cuerpo.

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

     

    time.sleep(retraso)

        







turtle.done()
