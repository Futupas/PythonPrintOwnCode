# pip.exe install Pillow

from PIL import Image

x = 1
y = 1

im = Image.open('test_image.png') # Can be many different formats.
pix = im.load()
print (im.size)  # Get the width and hight of the image for iterating over
print (pix[x,y])  # Get the RGBA Value of the a pixel of an image
pix[x,y] = (0, 0, 0)  # Set the RGBA Value of the image (tuple)
im.save('alive_parrot.png')  # Save the modified pixels as .png
