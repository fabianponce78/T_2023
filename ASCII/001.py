#-*- coding:utf-8 -*-
 
from PIL import Image
import argparse
 
# Procesamiento de parámetros de entrada de línea de comando
parser = argparse.ArgumentParser()
 
parser.add_argument ('archivo') # archivo de entrada
parser.add_argument ('- o', '- salida') # archivo de salida
parser.add_argument ('- width', type = int, default = 80) #output character width
parser.add_argument ('- height', type = int, default = 80) #Output character drawing height
 
#Obtener parámetros
args = parser.parse_args()
 
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output
 
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
 
 # Asigna 256 escala de grises a 70 caracteres
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
 
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]
 
if __name__ == '__main__':
 
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
 
    txt = ""
 
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
 
    print (txt)
    
         # Salida de pintura de personajes a archivo
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("#output.txt",'w') as f:
            f.write(txt)