# Crea un programa en Python que genere constantemente números aleatorios entre -10 y 10 
# y calcule su media constantemente. Con el objetivo de demostrar que la media es 0.

from random import randint

contador = 0;
suma = 0
while(True):
    numero = randint(-10, 10)
    suma  = suma + numero
    contador = contador + 1
    media = suma / contador
    print("{:.2f}".format(media))