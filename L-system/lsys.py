import numpy as np
import matplotlib.pyplot as plt
import random
import turtle

# variables: F+-[]
# axiom: F
# rules: (F → FF+[+F-F-F]-[-F+F+F])

# Test
# axiom = 'A'
# rules = {'A':'ABC','B':'A'}

axiom = 'F'
rules = {'F':'FF+[+F-F-F]-[-F+F+F]'}
# axiom = 'F'
# rules = {'F':'F+F−F−F+F'}

def generate(sentence, rules):
    newsentence = ''
    for i in range(len(sentence)):
        current = sentence[i]
        if current in rules:
            newsentence += rules[current]
        else:
            newsentence += current
    return newsentence

def parser(myturtle, sentence, angle):
    orig = np.array([0,0])
    stack  = [] 
    for i in sentence:
        current = i
        if current == 'F':
            myturtle.forward(5)
        elif current == '+':
            myturtle.right(angle)
            # myturtle.forward(10)
        elif current == '-':
            myturtle.left(angle)
            # myturtle.forward(10)
        elif current == '[':
            stack.append((myturtle.heading(), myturtle.pos()))
        
        elif current == ']':
            heading, position = stack.pop()
            myturtle.penup()
            myturtle.goto(position)
            myturtle.setheading(heading)
            myturtle.pendown()



x = axiom
for i in range(5):
    x = generate(x, rules)
# print(x, '\n')

t = turtle.Turtle()
t.color("white")
t.setposition(0,-300)
t.color("black")
t.pensize(1)
t.hideturtle()
wn = turtle.Screen()
wn.setup(width=0.8, height=0.8, startx=0, starty=0)

t.left(90)
t.speed(10)
turtle.tracer(0, 0)
parser(t,x, 25)
turtle.update()
turtle.getscreen().getcanvas().postscript(file='outputname.eps')


wn.exitonclick()