import turtle
import random

BOUNDARY_X = 300
BOUNDARY_Y = 300

paused = False

def turn_left():
    a.left(90)

def turn_right():
    a.right(90)

def turn_back():
    a.right(180)

def pause_game():
    global paused
    paused = not paused

def place_random_dot():
    x = random.randint(-BOUNDARY_X + 10, BOUNDARY_X - 10)
    y = random.randint(-BOUNDARY_Y + 10, BOUNDARY_Y - 10)
    dot_drawer.clear()
    dot_drawer.penup()
    dot_drawer.goto(x, y)
    dot_drawer.dot(15, "black")
    return x, y

def is_near(turtle, x, y, threshold=10):
    tx, ty = turtle.pos()
    return abs(tx - x) < threshold and abs(ty - y) < threshold

def update_score(score):
    score_display.clear() 
    score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

def game_over():
    a.hideturtle()
    score_display.hideturtle()
    game_over_display = turtle.Turtle()
    game_over_display.hideturtle()
    game_over_display.penup()
    game_over_display.goto(0, 0)
    game_over_display.write("Game Over", align="center", font=("Arial", 24, "bold"))

screen = turtle.Screen()
screen.bgcolor("red")
screen.setup(width=600, height=600)

a = turtle.Turtle()
a.penup()
a.shape("turtle")

dot_drawer = turtle.Turtle()
dot_drawer.hideturtle()

score_display = turtle.Turtle()
score_display.hideturtle() 
score_display.penup()
score_display.goto(0, 250)

dot_x, dot_y = place_random_dot()

x = 0
update_score(x)  

while x < 100:
    screen.listen()
    screen.onkey(turn_left, "Left")
    screen.onkey(turn_right, "Right")
    screen.onkey(turn_back, "Down")
    screen.onkey(pause_game, "p")
    
    if not paused:
        a.forward(1)
        
        if is_near(a, dot_x, dot_y):
            x += 1
            dot_x, dot_y = place_random_dot()
            update_score(x)  
        
        if abs(a.xcor()) > BOUNDARY_X or abs(a.ycor()) > BOUNDARY_Y:
            game_over()
            break

screen.mainloop()