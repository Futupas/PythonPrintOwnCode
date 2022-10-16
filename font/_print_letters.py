# letters = {
# 	'a': [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
# 	'!': [[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]],
# }

spaces_in_tab = 4
horizontal_margin = 0
vertical_margin = 1
letter_height = len(letters['a'])
letter_width = len(letters['a'][0])
char_1 = '#'
char_0 = ' '

src_text = 'hello world\nfrom Futupas'

def print_text(text):
    lines = text.split('\n')
    for line in lines:
        for letter_row_i in range(letter_height):
            for c in line:
                letter_bitmap = letters[c]
                letter_row = letter_bitmap[letter_row_i]
                line_to_print = ''.join(map(lambda x : (char_1 if x else char_0), letter_row))
                print(line_to_print, end=char_0*horizontal_margin)
            print()
        print('\n'*vertical_margin, end='')
                



print_text(src_text)
