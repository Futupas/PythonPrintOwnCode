from PIL import Image

real_pixel_size = 2 # then ALL data is in 'virtual pixels'
letter_width = 5
letter_height = 7
letter_horizontal_margin = 2
letter_vertical_margin = 2
padding_left = 1
padding_top = 1

letters_as_bitmap = {}

#  !"#$%&'()*+,-./01
# 23456789:;<=>?@ABC
# DEFGHIJKLMNOPQRSTU
# VWXYZ[\]^_`abcdefg
# hijklmnopqrstuvwxy
# z{|}~

letters_in_image = [
    [ ' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1' ],
    [ '2', '3', '4', '5', '6', '7', '8',  '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C' ],
    [ 'D', 'E', 'F', 'G', 'H', 'I', 'J',  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U' ],
    [ 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g' ],
    [ 'h', 'i', 'j', 'k', 'l', 'm', 'n',  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' ],
    [ 'z', '{', '|', '}', '~' ],
]

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


def get_letters_as_bitmap():
    image = Image.open('font/letters2.png').load()
    for ir in range(len(letters_in_image)):
        for ic in range(len(letters_in_image[ir])):
            letter = letters_in_image[ir][ic]
            x = padding_left + (letter_horizontal_margin + letter_width)*ic
            y = padding_top + (letter_vertical_margin + letter_height)*ir
            letters_as_bitmap[letter] = get_letter(image, x, y)


# x and y are virtual pixels
def get_letter(image, x, y):
    result = []
    for ir in range(letter_height):
        row = []
        result.append(row)
        for ic in range(letter_width):
            current_x = x + ic
            current_y = y + ir
            real_pixel_coords = convert_virtual_pixel_to_real(current_x, current_y)
            pixel_value = is_pixel_1(image[real_pixel_coords['x'], real_pixel_coords['y']])
            row.append(pixel_value)
    return result
            

def convert_virtual_pixel_to_real(x, y):
    return {
        'x': 2*x,
        'y': 2*y,
    }


def is_pixel_1(pixel):
    # in our image, white are the ones
    return pixel[0] > 128 and pixel[1] > 128 and pixel[2] > 128


# get_letters_as_bitmap()


def array_to_string(arr):
    arr_mapped = map(
        (lambda x: array_to_string(x) if hasattr(x, '__len__') else ('1' if x else '0')), 
        arr
    )
    return '[' + ','.join(arr_mapped) + ']'


def print_letters_to_py_file():
    get_letters_as_bitmap()
    file = open('font/test_file.py', 'w')
    file.write('letters = {\n')
    for i in letters_as_bitmap:
        letter = i
        if (letter == '\'' or letter == '\\'):
            letter = '\\' + letter
        letter_bitmap = letters_as_bitmap[i]

        string = '\t\'' + letter + '\': ' + array_to_string(letter_bitmap) + ',\n'
        file.write(string)
    file.write('}\n\n')
    file.write(open('font/print_letters.py', 'r').read())
    file.close()
    print('File ready')


print_letters_to_py_file()
