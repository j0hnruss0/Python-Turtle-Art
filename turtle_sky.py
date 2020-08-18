"""Turtle module based program that creates an image of a scene on the beach. Colors
   are somewhat random for the background but each image created is otherwise identical"""
import turtle
import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

def make_block(outline, fill, x, y, height):
    """Function to create the basic square shape that composes most of the image"""
    block = Turtle()
    block.speed(0)
    block.pensize(1)
    block.color(outline, fill)
    block.penup()
    block.setpos(x, y)
    block.pendown()
    block.hideturtle()

    block.begin_fill()
    for x in range(2):
        block.forward(25)
        block.right(90)
        block.forward(height)
        block.right(90)
    block.end_fill()

#The following two functions create the sky portion of the image    
def make_sky_row(pos_x, pos_y, height):
    for i in range(24):
        make_block((0, 255, 255),(random.randint(100, 255), 255, 241), pos_x, pos_y, height)
        pos_x += 25

def make_sunny_row(pos_x, pos_y, height):
    sun_index = 0
    for h in range(24):
        if sun_index < 4:
            make_block((0, 255, 255),(236, 240, random.randint(0, 150)), pos_x, pos_y, height)
        elif sun_index >= 4:
            make_block((0, 255, 255),(random.randint(150, 255), 255, 241), pos_x, pos_y, height)
        pos_x += 25
        sun_index += 1

# The next two functions handle the sea and the beach images
def make_sea_row(pos_x, pos_y, height):
    for j in range(24):
        make_block((0, 66, 209), (50, random.randint(0, 150), 209), pos_x, pos_y, height)
        pos_x += 25

def make_beach_row(pos_x, pos_y, height):
    for m in range(24):
        beach_color = (random.randint(230, 250), random.randint(150, 250), random.randint(10, 130))
        make_block((255, 187, 15), beach_color ,pos_x, pos_y, height)
        pos_x += 25

def make_sky(pos_x, pos_y, height):
    """Primary function to create the sky scene"""
    sky_row = 0
    for k in range(19):
        if sky_row < 15:
            make_sky_row(pos_x, pos_y, height)
        elif sky_row >= 15:
            make_sunny_row(pos_x, pos_y, height)
        pos_y += height
        sky_row += 1
        height += 1

def make_sea(pos_x, pos_y, height):
    """Primary function to create the sea scene"""
    for el in range(13):
        make_sea_row(pos_x, pos_y, height)
        pos_y -= height
        height +=1

def make_beach(pos_x, pos_y, height):
    """Primary function to create the beach scene"""
    for n in range(5):
        make_beach_row(pos_x, pos_y, height)
        pos_y -= height
        height += 1

def tree_trunk(x, y, width_1, width_2):
    """Constructs a three-sectored block as part of a palm tree foreground image"""
    tree = Turtle()
    tree.color((89, 40, 29), (193, 86, 62))
    tree.penup()
    tree.setpos(x, y)
    tree.pendown()
    tree.begin_fill()
    for x in range(2):
        tree.forward(width_1)
        tree.right(90)
        tree.forward(50)
        tree.right(90)
    tree.end_fill()

    tree.penup()
    tree.forward(width_1)
    tree.pendown()
    tree.color((89, 40, 29),(214, 144, 128))
    tree.begin_fill()
    for x in range(2):
        tree.forward(width_2)
        tree.right(90)
        tree.forward(50)
        tree.right(90)
    tree.end_fill()

    tree.penup()
    tree.forward(width_2)
    tree.pendown()
    tree.color((89, 40, 29), (193, 86, 62))
    tree.begin_fill()
    for x in range(2):
        tree.forward(width_1)
        tree.right(90)
        tree.forward(50)
        tree.right(90)
    tree.end_fill()
    tree.hideturtle()

def tree_whole(pos_x, pos_y, width_1, width_2):
    """Creates the trunk of the foreground palm tree"""
    for x in range(6):
        tree_trunk(pos_x, pos_y, width_1, width_2)
        pos_x -= 5
        pos_y +=50
        width_1 -=1
        width_2 -=1

def tree_leaves(start):
    """Draws the leaves and branches of the foreground palm tree"""
    pos_x = 155
    pos_y = 130
    stem = Turtle()
    stem.penup()
    stem.setpos(pos_x, pos_y)
    stem.pendown()
    
    stem.color((5, 112, 7))
    stem.right(start)
    for x in range(10):
        stem.forward(15)
        if start % 45 == 0:
            if start > 0 and start <= 90:
                leaf_pair(pos_x, pos_y, start + 65, start - 35)
                pos_x += 10.60660171779821
                pos_y -= 10.60660171779821
            elif start > 90 and start <= 180:
                leaf_pair(pos_x, pos_y, start + 45, start - 45)
                pos_x -= 10.60660171779821
                pos_y -= 10.60660171779821
            elif start > 180 and start <= 270:
                leaf_pair(pos_x, pos_y, start + 45, start - 45)
                pos_x -= 10.60660171779821
                pos_y += 10.60660171779821
            elif start > 270 and start <=360:
                leaf_pair(pos_x, pos_y, start + 55, start -5)
                pos_x += 10.60660171779821
                pos_y += 10.60660171779821
            elif start > 360:
                leaf_pair(pos_x, pos_y, start + 45, start - 45)
                pos_x += 10.60660171779821
                pos_y -= 10.60660171779821
            
    stem.hideturtle()

def leaf_pair(pos_x, pos_y, angle_1, angle_2):
    """Draws the leaves specifically, takes in different angle imputs 
       relative to the branches"""
    leaf = Turtle()
    leaf.penup()
    leaf.setpos(pos_x, pos_y)
    leaf.pendown()
    leaf.color((5, 112, 7),(40, 242, 13))

    leaf.begin_fill()
    leaf.right(angle_1)
    leaf.circle(150, 35)
    leaf.left(145)
    leaf.circle(150, 35)
    leaf.end_fill()
    leaf.hideturtle()

    leaf_2 = Turtle()
    leaf_2.penup()
    leaf_2.setpos(pos_x, pos_y)
    leaf_2.pendown()
    leaf_2.color((5, 112, 7),(40, 242, 13))

    leaf_2.begin_fill()
    leaf_2.right(angle_2)
    leaf_2.circle(150, 35)
    leaf_2.left(145)
    leaf_2.circle(150, 35)
    leaf_2.end_fill()
    leaf_2.hideturtle()
        

def main():
    """The entirety of the images created by the functions in the following order.
       The tree_named functions must come after the _sky, _sea, and_beach functions,
       as they will be drawn over the background, the tree_leaves functions are always last"""
    make_sky(-300, 10, 5)
    make_sea(-300, 5, 5)
    make_beach(-300, -138, 18)
    tree_whole(180, -120, 10, 20)
    tree_leaves(45)
    tree_leaves(135)
    tree_leaves(315)

    screen.mainloop()


if __name__ == "__main__":
    main()
