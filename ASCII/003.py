'''
Created on Jul 7, 2021

@author: Fabian Ponce
https://ichi.pro/es/convertir-una-imagen-en-ascii-con-python-260896610350679
'''

from PIL import Image

pict = Image.open('mm.jpg')
pict = Image.open('APEX.png')
height, width = pict.size
aspect_ratio = height/width

# print(f'height: {height}px and width: {width}px')

new_width = 240
new_height = aspect_ratio * new_width*0.5
pict = pict.resize((new_width, int(new_height)))
pict = pict.convert('L')
pixels = pict.getdata()
chars = ["i", "o", "#", "%", "!", "-", ":", ":", "&", "*", "i"]
new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)
new_pixels_count = len(new_pixels)
ascii_picture = [new_pixels[index:index+new_width]
                 for index in range(0, new_pixels_count, new_width)]
ascii_picture = "\n".join(ascii_picture)

with open('ascii_picture.txt', 'w') as file:
    file.write(ascii_picture)
