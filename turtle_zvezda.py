from turtle import *
hideturtle()

def draw_star(sidesize, points, alfacorner):
    betacorner = 360/points+alfacorner
    begin_fill()
    for x in range(points*2):
        forward(sidesize)
        if x % 2 == 0:
            left(180-alfacorner)
        else:
            right(180-betacorner)
    end_fill()

draw_star(70,20, 30)