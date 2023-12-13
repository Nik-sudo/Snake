import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Window set up
wn = turtle.Screen()
wn.title("Snake game by Nik")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 260)

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Ariel", 24, "normal"))

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    match head.direction:
        case "up":
            head.sety(head.ycor() + 20)
        
        case "down":
            head.sety(head.ycor() - 20)
        
        case "left":
            head.setx(head.xcor() - 20)
        
        case "right":
            head.setx(head.xcor() + 20)

# Bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

body_seg = []

# Game end
def game_over():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for seg in body_seg:
        seg.goto(1000, 1000)

    body_seg.clear()

    score = 0
    delay = 0.1

    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Ariel", 24, "normal"))

    
# Game loop
while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_over()
        score = 0

    if head.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("blue")
        new_body.penup()
        body_seg.append(new_body)

        delay -= 0.001
        score += 1
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Ariel", 24, "normal"))
    
    for index in range(len(body_seg)-1, 0, -1):
        body_seg[index].goto(body_seg[index-1].xcor(), body_seg[index-1].ycor())
    if len(body_seg) > 0:
        body_seg[0].goto(head.xcor(), head.ycor())
    move()

    for seg in body_seg:
        if seg.distance(head) < 20:
            game_over()
            score = 0
    
    time.sleep(delay)

# Ensures window stays open
wn.mainloop()