# letters = {
# 	' ': [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
# 	'!': [[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]],
# }

def print_letter_to_console(letter):
    width = len(letter[0])
    height = len(letter)
    print('+' + '-'*width + '+')
    for ir in range(height):
        print('|', end='')
        for ic in range(width):
            if (letter[ir][ic]):
                print('#', end='')
            else:
                print(' ', end='')
        print('|')
    print('+' + '-'*width + '+')

for i in letters:
    letter = letters[i]
    print(i + ':')
    print_letter_to_console(letter)
    print()

print('ready')
