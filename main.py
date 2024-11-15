
from setup import start_screen,my_turtle,end_pos,screen_scene
import random
from mp3 import  announcement

start_position=[-20,-10,0,10,20]
bet_color=start_screen()

run=True

while run:

    move=random.choice(my_turtle)
    move.speed("fast")
    move.pendown()
    move.fd(random.randint(0,10))
    if move.xcor()>=end_pos:
        run=False
        winning_color=move.pencolor()
        if winning_color==bet_color:
            announcement(" you won the race")
            print("\"you won the race\"")
        else:
            announcement("you lost the race")
            print("\"you won the race\"")


screen_scene.exitonclick()