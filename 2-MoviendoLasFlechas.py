
import turtle
import time
retraso = 0.1

#Definimos el entorno de nuestro juego

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("gray")
s.title("Proyecto La Viborita")

#A continuación daremos algunas cualidades a nuestro personaje

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = 'stop'
serpiente.color("green")


#Definimos las DIRECCIONES del movimiento.

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


#Definimos el MOVIMIENTO de nuestra serpiente.

def movimiento():
    if serpiente.direction == 'up':
        y = serpiente.ycor()
        serpiente.sety(y + 20)         #Con esto le decimos que se mueva sobre la coordenada Y más 20 pixeles. Y así con cada coordenada
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
    movimiento()
    time.sleep(retraso)

        


turtle.done()
