import turtle
import random
import time 

def turtle_race():
    screen = turtle.Screen()
    screen.bgcolor("lightgreen")
    screen.title("5 Turtle race game")


    #Crate race track
    track = turtle.Turtle()
    track.speed(0) 
    track.penup()

    #start line
    track.goto(-300, 150)
    track.pendown()
    track.color("red")
    track.width(3)
    track.goto(-300, -150)

    #finish line
    track.penup()
    track.goto(300, 150)
    track.pendown()
    track.color("blue")
    track.width(3)
    track.goto(300, -150)

    #creat turtles
    colors = ["black", "white", "blue", "yellow", "purple"] 
    turtles = []

    for i, color in enumerate(colors):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(color)
        t.penup()
        t.goto(-320, 100 - i * 40)
        turtles.append(t)

    #countdown
    countdown = turtle.Turtle()
    countdown.penup()
    countdown.hideturtle()
    countdown.goto(0, 200)
    
    for i in range(3, 0, -1):
        countdown.write(str(i), align="center", font=("Arial", 48, "normal"))
        time.sleep(1)
        countdown.clear()
        
    countdown.write("Go!", align="center", font=("Arial", 48, "normal"))
    time.sleep(0.5)
    countdown.clear()
    
    #race
    winner = None
    while not winner:
        for t in turtles:
            #move turtle forward by random distance
            distance = random.randint(1, 10)
            t.forward(distance)
            #check for winner
            if t.xcor() >= 300:
                winner = t
                break
    #announce winner
    countdown.goto(0, 0)
    countdown.color(winner.color()[0])
    countdown.write(f"The winner is the {winner.color()[0]} turtle!", align="center", font=("Times New Roman", 24, "normal"))
         
        
    screen.mainloop()
    
turtle_race()