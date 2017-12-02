# 
# 2) Crea un script llamado tabla.py que realice las siguientes tareas:
# Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
# El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
# En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
# El script contendrá un bucle for que itere el número de veces del primer argumento.
# Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
# Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (end='' evita el salto de línea).
# Ejecuta el código y observa el resultado.
# Ahora intenta deducir dónde y cómo añadir otra instruccion print para dibujar una tabla.
# Recordatorio: Los argumentos se envían como cadenas separadas por espacios, si quieres enviar varias palabras como un argumento deberás indicarlas entre comillas dobles "esto es un argumento".
#  Para capturar los argumentos debes utilizar el módulo sys y su lista argv:
# import sys
# print(sys.argv) # argumentos enviados

import sys

if len(sys.argv) == 3: 
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    if  1 > filas > 9 or 1 > columnas > 9:
        print("Erro - O número de Filas ou columnas é incorrecto debe estar entre 1 e 9")
    else:
        # Aqui empieza la lógica
        for f in range(filas):
            print("")
            for c in range(columnas):
                print(" * ", end="")

else:
    print("Erro - Número de argumentos incorrecto. ")
    print("Indique o nome do ficheiro, a filas e as columnas:")
    print(" tabla.py [1-9] [1-9]")
