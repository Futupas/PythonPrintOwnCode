from PIL import Image

real_pixel_size = 2 # then ALL data is in 'virtual pixels'
real_pixel_size = 2
letter_width = 5
letter_height = 7
letter_vertical_margin = 2
letter_horizontal_margin = 2
padding_left = 1
padding_top = 1

letter_test = [
    [ 0, 0, 0, 1, 0 ],
    [ 0, 0, 0, 1, 0 ],
    [ 0, 1, 1, 1, 0 ],
    [ 0, 0, 0, 1, 0 ],
    [ 0, 0, 0, 1, 0 ],
    [ 0, 0, 0, 1, 0 ],
    [ 0, 0, 0, 1, 0 ],
    [ 1, 1, 1, 1, 1 ],
]

letters_as_bitmap = {}

#  !"#$%
# 234567
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

print_letter_to_console(letter_test)


def letters_as_bitmap():
    image = Image.open('letters2.png').load()
    

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


a = get_letter(Image.open('font/letters2.png').load(), 8, 1)
print_letter_to_console(a)

# im = Image.open('letters2.png')
# pix = im.load()
# pix[0, 0].
# print (im.size)  # Get the width and hight of the image for iterating over
# print (pix[x,y])  # Get the RGBA Value of the a pixel of an image
# pix[x,y] = (0, 0, 0)  # Set the RGBA Value of the image (tuple)
# im.save('alive_parrot.png')  # Save the modified pixels as .png