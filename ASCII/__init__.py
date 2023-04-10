# -*- coding: utf-8 -*-

#encoding=utf-8

from PIL import Image

IMG = "C:/#_FP_APEX/#_DEV/#_Py_FP/Py_Test/ASCII/Apex_logo_horizontal_color.png"
IMG = "C:/#_FP_APEX/#_DEV/#_Py_FP/Py_Test/ASCII/Apex.png"
WIDTH = 180
HEIGHT = 100
OUTPUT = "C:/#_FP_APEX/#_DEV/#_Py_FP/Py_Test/ASCII/test.txt"

# <----------------- Procesando im�genes -------------->

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# La relaci�n de mapeo entre personajes y RGB
def get_char(r,g,b,alpha=256):
    if alpha == 0 :
        return ' '
    lenght = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/lenght
    return ascii_char[int(gray/unit)]

#Si se ejecuta por s� solo, ejecute lo siguiente, si es un m�dulo importado, no se ejecutar�
if __name__ == '__main__':
    im = Image.open(IMG)
    # Aqu� est� el tama�o de la imagen convertida, y luego el segundo par�metro representa la calidad de la imagen, hay 4 tipos, Imagen de baja calidad. NEARSET, Imagen bilineal. BILINEAR, Imagen de interpolaci�n spline c�bica.
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    txt = ""

    for h in range(HEIGHT):
        for w in range(WIDTH):
            # im.getpixel: Obtenga los tres valores de r, gyb correspondientes a RGB seg�n las coordenadas. Aqu�, los dos corchetes de getpixel ((i, j)) son muy importantes
            txt += get_char(*im.getpixel((w,h)))
        txt += '\n'
    print(txt)

# Salida de caracteres a archivo
if OUTPUT:
    with open(OUTPUT,'w') as f:
        f.write(txt)
else:
    with open("output.txt",'w') as f:
        f.write(txt)