# Reaction Time Test
# By: Diana Sousa | dianasousa.pt
# Ninja Turtles Race
# Introduction: This simple tests will give us data about participants reaction time 
#             in order to study in future User Experience, time reactions in Serious Games.
#             This project was born during a research about programming electronics with
#             Python and Raspberry Pi; applying contents learned
#             during classes and obtained during the research papper.

# imports
import turtle
import random

from gpiozero import LED,Button,Buzzer
from time import time, sleep
from random import randint
from random import uniform
from turtle import *
from signal import pause

### defining electronic components
led = LED(17)     # led1stTest (color red)
btn4 = Button(4)  # button4  ok > Donatello
btn3 = Button(22) # button22 ok > Raphael
btn2 = Button(11) # button11 ok > Leonardo
btn1 = Button(6)  # button6  ok > Raphael
buzzer = Buzzer (26)

## window setup
window = turtle.Screen()
window.title("Ninja Turtles Race")
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()


## defining game objects
# players
turtles = 4

# dirt
# dirt header
turtle.setpos(-410,120)
turtle.color("chocolate")
turtle.pendown()

for i in range(4):
  turtle.begin_fill()
  turtle.forward(380)
  turtle.left(90)
  turtle.forward(10)
  turtle.left(90)
  turtle.forward(380)
  turtle.left(90)
  turtle.forward(10)
  turtle.left(90)
  turtle.end_fill()

# dirt bottom
turtle.setpos(-410,-20)
turtle.color("chocolate")
turtle.pendown()

for i in range(4):
  turtle.begin_fill()
  turtle.forward(380)
  turtle.left(90)
  turtle.forward(10)
  turtle.left(90)
  turtle.forward(380)
  turtle.left(90)
  turtle.forward(10)
  turtle.left(90)
  turtle.end_fill()

# finish line square stamps
stamp_size = 40
square_size = 13
finish_line = -50
turtle.color("green", "chocolate",)
turtle.shape("square")
turtle.shapesize(square_size/stamp_size)
turtle.penup()
for i in range (5):
  turtle.setpos(finish_line, 50-(50 - (i * square_size * 2)))
  turtle.stamp()
  turtle.setpos(finish_line+10, 60-(50 - (i * square_size * 2)))
  turtle.stamp()
  turtle.setpos(finish_line+20, 50-(50 - (i * square_size * 2)))
  turtle.stamp()

# players by turtles @ race
turtle.shape("arrow")
speed(0)
penup()
goto(-350, 140)
turtle.color("white")
for step in range(15):
  write(step, align='center')
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

# raphael
raphael = Turtle()
raphael.color("red")
raphael.shape("turtle")
raphael.penup()
raphael.goto(-380, 100)
raphael.pendown()
turtle.goto(-350,-250)  
sample = turtle.Turtle()
pen = sample.getpen()
pen.color("white")
pen.write("Hello! I am Raphael!", font=("Calibri", 16, "bold"))
sleep(2)
pen.clear()
pen.penup()
for turn in range(10):
  raphael.right(36)

# leonardo
leonardo = Turtle()
leonardo.color("blue")
leonardo.shape("turtle")
leonardo.penup()
leonardo.goto(-380, 70)
leonardo.pendown()
turtle.goto(-350,-250)  
sample = turtle.Turtle()
pen = sample.getpen()
pen.color("white")
pen.write("Hello! I'm Leonardo", font=("Calibri", 16, "bold"))
sleep(2)
pen.clear()
pen.penup()
for turn in range(72):
  leonardo.left(5)

# michelangelo
michelangelo = Turtle()
michelangelo.color("orange")
michelangelo.shape("turtle")
michelangelo.penup()
michelangelo.goto(-380, 40)
michelangelo.pendown()
turtle.goto(-350,-250)
sample = turtle.Turtle()
pen = sample.getpen()
pen.color("white")
pen.write("Hi! I'm Michelangelo", font=("Calibri", 16, "bold"))
sleep(2)
pen.clear()
pen.penup()
for turn in range(60):
  michelangelo.right(6)

# donatello
donatello = Turtle()
donatello.color("purple")
donatello.shape("turtle")
donatello.penup()
donatello.goto(-380, 10)
donatello.pendown()
turtle.goto(-350,-250)  
sample = turtle.Turtle()
pen = sample.getpen()
pen.color("white")
pen.write("Hello! I'm Donatello", font=("Calibri", 16, "bold"))
sleep(2)
pen.clear()
pen.penup()
for turn in range(30):
  donatello.left(12)

# Prepare players
pen = sample.getpen()
pen.penup()
pen.goto(-350,-250)
pen.pendown()
pen.write("\n :::: When the Led lights up, immediately press the button \n to test your reaction time. :::: \n", font=("Calibri", 16, "bold"))
sleep(2)
pen.clear()
pen.penup()

pen = sample.getpen()
pen.penup()
pen.goto(-350,200)
pen.pendown()
pen.write("Ready?", font=("Calibri", 16, "bold"))
sleep(2)
pen.clear()
pen.penup()

pen = sample.getpen()
pen.penup()
pen.goto(-200,200)
pen.pendown()
pen.write("Set...", font=("Calibri", 16, "bold"))
sleep(2)
pen.clear()
pen.penup()

# reaction time
def reaction_time():
    
    # arrays
    values1 = []
    values2 = []
    values3 = []
    values4 = []
    
    # number of times to go forward in the same game to collect time reaction values
    numberGame1 = 0
    numberGame2 = 0
    numberGame3 = 0
    numberGame4 = 0
      
    # buzzer to send a small noise to activate the players sense reactions (audition)
    ## sleep(randint(1,10))
    buzzer.beep(0.5, 0.5)
    sleep(5)
    buzzer.off()
##    sleep(1)
    
##    pause()
    
    # led to comunicate that the players can start each click button (visual: light: with a led)
    sleep(randint(1,10))
    led.on()
    
    # text on the screen (visual: text: on the screen)
    pen = sample.getpen()
    pen.penup()
    pen.goto(-80,200)
    pen.pendown()
    pen.write("Go!", font=("Calibri", 16, "bold"))
    sleep(2)
    pen.clear()
    
    # game code and information to display on the shell
    begin = time()
    print("Red led turned on at ", begin, " seconds")
    
    while (numberGame1 < 7 and numberGame2 < 7 and numberGame3 < 7 and numberGame4 < 7):                                                                                                           

        # btn1
        if btn1.is_pressed:
            raphael.forward(50)
            led.off()
            end1 = time()
            print("Red led turned off at ", end1, " seconds")
            print("---------------------------")
            print("Reaction Time for P1:")
            reactiontime1 = end1-begin
            print(reactiontime1, "seconds \n")
            values1.append(reactiontime1)
            print(values1)
            numberGame1 = numberGame1+1
            continue
        

        # btn2
        if btn2.is_pressed:
            leonardo.forward(50)
            led.off()
            end2 = time()
            print("Red led turned off at ", end2, " seconds")
            print("---------------------------")
            print("Reaction Time for P2:")
            reactiontime2 = end2-begin
            print(reactiontime2, "seconds \n")
            values2.append(reactiontime2)
            print(values2)
            numberGame2 = numberGame2+1
            continue
        

        # btn3
        if btn3.is_pressed:
            michelangelo.forward(50)
            led.off()
            end3 = time()
            print("Red led turned off at ", end3, " seconds")
            print("---------------------------")
            print("Reaction Time for P3:")
            reactiontime3 = end3-begin
            print(reactiontime3, "seconds \n")
            values3.append(reactiontime3)
            print(values3)
            numberGame3 = numberGame3+1
            continue
        

        # btn4
        if btn4.is_pressed:
            donatello.forward(50)
            led.off()
            end4 = time()
            print("Red led turned off at ", end4, " seconds")
            print("---------------------------")
            print("Reaction Time for P4:")
            reactiontime4 = end4-begin
            print(reactiontime4, "seconds \n")
            values4.append(reactiontime4)
            print(values4)
            numberGame4 = numberGame4+1
            continue

    if (numberGame1 == 7):
        print("\n :::: Winner: Raphael  :::: \n")
        turtle.goto(-350,-250) 
        turtle.write("\n :::: And the Winner is: Raphael  :::: \n Congrats!", font=("Calibri", 16, "bold"))
    if (numberGame2 == 7):
        print("\n ::::  Winner: Leonardo ::::  \n")
        turtle.goto(-350,-250) 
        turtle.write("\n :::: And the Winner is: Leonardo  :::: \n Congrats!", font=("Calibri", 16, "bold"))
    if (numberGame3 == 7):
        print("\n  :::: Winner: Michelangelo  :::: \n")
        turtle.goto(-350,-250) 
        turtle.write("\n :::: And the Winner is: Michelangelo  :::: \n Congrats!", font=("Calibri", 16, "bold"))
    if (numberGame4 == 7):
        print("\n  :::: Winner: Donatello  :::: \n")
        turtle.goto(-350,-250) 
        turtle.write("\n :::: And the Winner is: Donatello  :::: \n Congrats!", font=("Calibri", 16, "bold"))
        
    # set a reaction time table on our shell <=> data to be collect for our research
    # btn1 values
    maximum1 = max(values1)
    minimum1 = min(values1)
    media1 = sum(values1)/len(values1)

    # btn2 values
    maximum2 = max(values2)
    minimum2 = min(values2)
    media2 = sum(values2)/len(values2)

    # btn3 values
    maximum3 = max(values3)
    minimum3 = min(values3)
    media3 = sum(values3)/len(values3)
    
    # btn4 values
    maximum4 = max(values4)
    minimum4 = min(values4)
    media4 = sum(values4)/len(values4)

    # reaction time winner > who had minimum reaction time 
    minimum = min(minimum1,minimum2,minimum3,minimum4)
    
    # reaction time panel
    print("#------------------------------------------------------------#")
    print("#                       Reaction Time Test                   #")
    print("#------------------------------------------------------------#")
    print(" Id \t Maximum \t    Minimum \t    Media")
    print("------------------------------------------------------------")
    print(" %s \t %fs \t %fs \t %fs" % (str(btn1.pin.number), maximum1, minimum1, media1))
    print(" %s \t %fs \t %fs \t %fs" % (str(btn2.pin.number), maximum2, minimum2, media2))
    print(" %s \t %fs \t %fs \t %fs" % (str(btn3.pin.number), maximum3, minimum3, media3))
    print(" %s \t %fs \t %fs \t %fs" % (str(btn4.pin.number), maximum4, minimum4, media4))
    print("------------------------------------------------------------")
    print(" \n The ninja with the best reaction time is the one who got: \t %fs. \n" % (minimum))

print("When the Led lights up, immediately press the button to test your reaction time. \n")
reaction_time()
print("#------------------------------------------------------------#")
print("#                             End                            #")
print("#------------------------------------------------------------#")