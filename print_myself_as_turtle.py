# Made with ♡ by Futupas

import os
import turtle
from letters import letters

turtle.Screen().title('Self-writing turtle: loading')

REAL_PEN_SIZE = 20 # Found in google
pixel_size = 4 # Then all measurements in 'virtual' pixels
spaces_in_tab = 4
margin_horizontal = 0
margin_vertical = 1
letter_height = len(letters['a'])
letter_width = len(letters['a'][0])
char_1 = '#'
char_0 = ' '
padding_vertical = 3
padding_horizontal = 3
# turtle_speed = 10 # 1..10
turtle_speed = 'fastest'
hide_turtle = False



file_path = os.path.abspath(__file__)
# file = open('.gitignore', 'r', encoding='utf-8')
file = open(file_path, 'r', encoding='utf-8')
file_contents = file.read().replace('\r', '')
lines = file_contents.split('\n')

text_height = len(lines)
text_width = max(map(lambda x : len(x), lines))

# Yes, (margin_vertical-1) is more correct, but I do't wanna check last margin in loop, so it's a kind of kostyl
screen_width = 2 * padding_horizontal + text_width * (letter_width + margin_horizontal)
screen_height = 2 * padding_vertical + text_height * (letter_height + margin_vertical)

turtle.getscreen().screensize(
    pixel_size * screen_width, 
    pixel_size * screen_height
)
turtle.shape('square')
turtle.shapesize(pixel_size / REAL_PEN_SIZE, pixel_size / REAL_PEN_SIZE, 0)
turtle.pencolor(0, 0, 0)
turtle.fillcolor(0, 0, 0)
turtle.speed(turtle_speed)
if hide_turtle:
    turtle.hideturtle()
ts = turtle.getscreen().getcanvas()
ts.xview_moveto(pixel_size * screen_width / -2)
ts.yview_moveto(pixel_size * screen_height / -2)
turtle.penup()

def draw_pixel():
    turtle.stamp()

def goto_line(line_index, pseudo_index_inside_line):
    real_x = pixel_size * (padding_horizontal)
    real_y = pixel_size * (padding_vertical + line_index * (letter_height + margin_vertical) + pseudo_index_inside_line)

    # Because 0,0 is in the center
    real_x = real_x - (screen_width*pixel_size/2 + pixel_size / 2)
    real_y = (screen_height*pixel_size/2 - pixel_size / 2) - real_y

    # turtle.setpos(real_x, real_y)
    turtle.setposition(real_x, real_y)


def print_text(lines):
    for line_i in range(len(lines)):
        line = lines[line_i].replace('\t', ' '*spaces_in_tab)
        for letter_row_i in range(letter_height):
            goto_line(line_i, letter_row_i)
            for c in line:
                letter_bitmap = letters[c]
                letter_row = letter_bitmap[letter_row_i]
                for px in letter_row:
                    if (px):
                        draw_pixel()
                    turtle.forward(pixel_size)
                turtle.forward(pixel_size * margin_horizontal)


turtle.getscreen().title('Self-writing turtle: writing')

print_text(lines)

turtle.getscreen().title('Self-writing turtle')

turtle.done()
