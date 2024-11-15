from turtle import Turtle, Screen
import random
from mp3 import announcement


colours=["red","yellow","green", "gold", "violet"]
start_pos=[-100,-50,0,50,100]
end_pos=350
start_trigger=(-350,100)
my_turtle=[]
screen_scene=Screen()

def start_screen():
    screen = Screen()
    announcement("Choose  a color from 'red,yellow,green,Gold,Violet' for your turtle")
    bet_color = screen.textinput(title="Turtle Race", prompt="Choose  a color from 'red,yellow,green,Gold,Violet' for your turtle").lower()
    line = Turtle()
    line.speed("fast")
    line.penup()
    line.goto(x=350, y=-300)
    line.left(90)
    line.pendown()
    line.pensize(5)
    line.fd(600)
    return bet_color

for i in range(5):

    turtle = Turtle()
    turtle.penup()
    turtle.shape("turtle")
    turtle.color(colours[i])
    turtle.goto(-350, start_pos[i])
    current_pos=turtle.pos()
    my_turtle.append(turtle)

