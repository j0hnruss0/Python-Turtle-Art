"""Turtle module program that creates a semi-random abstract image containing gem-shaped
   blocks and bands. No two images created are alike"""
import turtle
import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

def diamond_square(pos_x, pos_y, size_set):
    """Creates the gem-shaped blocks for the foreground bands.
       Colors are changed using the color_change function input"""
    color_counter = 0
    alpha = turtle.Turtle()
    alpha.color('black')
    alpha.pensize(1)
    alpha.speed(0)
    alpha.penup()
    alpha.setpos(pos_x, pos_y)
    alpha.pendown()
    alpha.hideturtle()


    for all in range(4):
        alpha.right(45)
        alpha.fillcolor(color_change(color_counter))
        alpha.begin_fill()
        alpha.forward(7.071067811865475)
        alpha.right(45)
        alpha.forward(size_set - 10)
        alpha.right(45)
        alpha.forward(7.071067811865475)
        alpha.right(135)
        alpha.forward(size_set)
        alpha.end_fill()
        alpha.right(90)
        alpha.forward(size_set)
        alpha.right(90)
        color_counter += 1

    alpha.penup()
    alpha.setpos(pos_x +5, pos_y - 5)
    alpha.pendown()
    alpha.fillcolor(color_change(4))
    alpha.begin_fill()
    for all in range(4):
        alpha.forward(size_set - 10)
        alpha.right(90)
    alpha.end_fill()

def background_block(pos_x, pos_y):
    """Creates the background scene of green-toned bricks. Color is
       slightly altered for each brick"""
    beta = Turtle()
    beta.color((0, 51, 51))
    beta.pensize(1)
    beta.speed(0)
    beta.penup()
    beta.setpos(pos_x, pos_y)
    beta.pendown()
    beta.hideturtle()

    beta.fillcolor((0, random.randint(55, 130), random.randint(15, 50)))
    beta.begin_fill()
    for all in range(2):
        beta.forward(30)
        beta.right(90)
        beta.forward(15)
        beta.right(90)
    beta.end_fill()
                
def background_row(pos_x, pos_y):
    """Creates one row for the background scene"""
    for all in range(30):
        background_block(pos_x, pos_y)
        pos_x += 30

# The following two functions create the horizontal and verticle bands of the foreground
def make_rows(pos_x, pos_y, size_set):
    for all in range(90 - size_set):
        diamond_square(pos_x, pos_y, size_set)
        pos_x += size_set
    

def make_columns(pos_x, pos_y, size_set):
    for all in range(90 - size_set):
        diamond_square(pos_x, pos_y, size_set)
        pos_y += size_set
    
def color_change(counter):
    """Semi-randomizes the colors used for the foreground gem-blocks. The colors
       use the rgb-scale and are various shades and tints of yellow and purple"""
    use_color = ''
    if counter == 0:
        use_color = (255, 255, random.randint(0, 100))
    elif counter == 1:
        use_color = (255, 255, random.randint(125, 230))
    elif counter == 2:
        use_color = (255, random.randint(200, 224), random.randint(0, 100))
    elif counter == 3:
        use_color = (255, random.randint(120, 140), random.randint(0, 30))
    elif counter == 4:
        use_color = (random.randint(100, 160),
                     random.randint(0, 60),
                     random.randint(180, 255))
    
    return use_color

def background_full(pos_x, pos_y):
    """Creates the entirety of the background pattern"""
    for all in range(21):
        background_row(pos_x, pos_y)
        background_row(pos_x + 15, pos_y - 15)
        pos_y -= 30

def make_bands():
    """This final functions alternately creates rows and columns of the gem-shaped
       squares for the background. Five rows and columns are made each, the width
       of each row/column is random"""
    for all in range(5):
        make_rows(-350, random.randint(-250, 250), random.randint(20, 80))
        make_columns(random.randint(-250, 250), -300, random.randint(20, 80))
        
        
#make_rows(-400, 20, 40)
#make_columns(30, -400, 50)
background_full(-400, 275)
make_bands()


