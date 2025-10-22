import turtle as t
import random as rd

# 🌟 Setup screen
t.title("Caterpillar Game")
t.bgcolor('#9be564')   # light green background
t.setup(width=800, height=600)

# 🐛 Caterpillar
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('#023047')   # dark blue
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

# 🍁 Leaf
leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('red')
leaf.penup()
leaf.hideturtle()
leaf.speed()

# ✨ Game status
game_started = False
caterpillar_speed = 2
caterpillar_length = 3
score = 0

# 📜 Text turtle for messages
text_turtle = t.Turtle()
text_turtle.hideturtle()
text_turtle.color('black')
text_turtle.penup()
text_turtle.sety(100)
text_turtle.write('🐛 Caterpillar Game 🐛\nPress SPACE to Start',
                  align='center', font=('Arial', 24, 'bold'))

# 🏆 Score turtle
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = caterpillar.pos()
    return x < left_wall or x > right_wall or y > top_wall or y < bottom_wall

def game_over():
    global game_started
    caterpillar.hideturtle()
    leaf.hideturtle()
    text_turtle.clear()
    text_turtle.sety(0)
    text_turtle.write('💀 GAME OVER 💀\nPress SPACE to Restart',
                      align='center', font=('Arial', 28, 'bold'))
    game_started = False

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2) - 100
    y = (t.window_height()/2) - 80
    score_turtle.setpos(x,y)
    score_turtle.write("Score: " + str(current_score),
                       align='right', font=('Arial', 20, 'bold'))

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def start_game():
    global game_started, caterpillar_speed, caterpillar_length, score
    if game_started:
        return
    game_started = True
    
    score = 0
    caterpillar_speed = 2
    caterpillar_length = 3

    text_turtle.clear()
    caterpillar.color('#023047')
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.goto(0,0)
    caterpillar.setheading(0)
    caterpillar.showturtle()

    display_score(score)
    place_leaf()

    move_caterpillar()

def move_caterpillar():
    global caterpillar_length, caterpillar_speed, score
    if game_started:
        caterpillar.forward(caterpillar_speed)

        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length += 1
            caterpillar.shapesize(1,caterpillar_length,1)
            caterpillar_speed += 1
            score += 10
            display_score(score)

        if outside_window():
            game_over()
        else:
            t.ontimer(move_caterpillar, 100)  # call itself every 100 ms

def move_up():
    if caterpillar.heading() != 270:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() != 90:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() != 0:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() != 180:
        caterpillar.setheading(0)

# 🎮 Controls
t.listen()
t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')

t.mainloop()
