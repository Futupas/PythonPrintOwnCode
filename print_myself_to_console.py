import os
from letters import letters

spaces_in_tab = 4
horizontal_margin = 0
vertical_margin = 1
letter_height = len(letters['a'])
letter_width = len(letters['a'][0])
char_1 = '#'
char_0 = ' '

def print_text(text):
    lines = text.split('\n')
    for line in lines:
        real_line = line.replace('\t', ' '*spaces_in_tab)
        for letter_row_i in range(letter_height):
            for c in real_line:
                letter_bitmap = letters[c] if (c in letters) else letters['unknown']
                letter_row = letter_bitmap[letter_row_i]
                line_to_print = ''.join(map(lambda x : (char_1 if x else char_0), letter_row))
                print(line_to_print, end=char_0*horizontal_margin)
            print()
        print('\n'*vertical_margin, end='')
                


file_path = os.path.abspath(__file__)
file = open(file_path, 'r')
file_contents = file.read().replace('\r', '')
print_text(file_contents)
