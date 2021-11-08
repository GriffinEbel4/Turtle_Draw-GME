from os import close
import turtle 
from turtle import Screen, Turtle
import math

TDTXT = input("Please enter a file name to draw: ")

turtlescreen = turtle.Screen()
turtlescreen.setup(450, 450)

total_distance = 0
previous_point = []
current_point = []

def close():
    turtlescreen.onkeypress(turtlescreen.bye,
    "Enter")
    close = Turtle()
    close.hideturtle()
    close.write("Press Enter to close")

print(math.dist(previous_point, current_point))

draw = turtle.Turtle()
draw.speed(10)
draw.penup()

text_file = open(TDTXT, 'r')
line = text_file.readline()

while line:
    print (line, end='')
    parts = line.split(' ')

    if len(parts) == 3:
        color = parts[0]
        x= int(parts[1])
        y = int(parts[2]) 
        if draw.pendown:
            starting_point= [0,0]
            current_point = [x, y] 
            distance = (math.dist(starting_point, current_point))  
            print (distance)
            total_distance += distance
            starting_point = current_point
            
        draw.color(color)
        draw.goto(x,y)
        draw.pendown()

    if len(parts) == 1:
        draw.penup()

    line = text_file.readline()

turtle.write('Total Distance:' + str(total_distance))
    
close
turtle.mainloop()



