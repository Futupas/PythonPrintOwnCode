from PIL import Image

real_pixel_size = 2 # then ALL data is in 'virtual pixels'
letter_width = 5
letter_height = 7
letter_horizontal_margin = 2
letter_vertical_margin = 2
padding_left = 1
padding_top = 1

letters_as_bitmap = {}

letters_in_image = [
    # [ '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ]
    [ ' ', '!', '"', '#', '$', '%' ],
    [ '2', '3', '4', '5', '6', '7' ],
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


get_letters_as_bitmap()
for i in letters_as_bitmap:
    letter = letters_as_bitmap[i]
    print(i + ':')
    print_letter_to_console(letter)
    print()

print('hello world')
