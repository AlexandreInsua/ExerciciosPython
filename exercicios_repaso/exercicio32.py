# Programa en python (llamado QueDiaEsHoy) que muestre la fecha de hoy por pantalla al ser ejecutado.
#  Además guardará esa fecha en un fichero de registro.
# Si el programa se ejecuta por consola con la opción -l, mostrará todas las fechas guardadas 
# en ese fichero de registro. Ej QueDiaEsHoy -l 

from datetime import *
import time
import sys
import os.path
import os

rutaFichero="fechas.txt"

numParametros = len(sys.argv)
if numParametros == 1:
    fecha = datetime.today()
    print( fecha )

    print( time.strftime("%d/%M/%Y") )

    fichero = open(rutaFichero,"a")
    fichero.write( str(fecha) + "\n" )
    fichero.close()
elif(numParametros == 2):
    if sys.argv[1] == "-l":
        if not os.path.isfile(rutaFichero):
            print("Fichero vacio")
            exit()
        fichero = open(rutaFichero, "r")
        lineas = fichero.readlines()
        for linea in lineas:
            print(linea)
        fichero.close()
    elif sys.argv[1] == "-d":
        if os.path.isfile(rutaFichero):
            os.remove(rutaFichero)
        print("Registro limpiado")
    else:
        print("El parámetro tiene que ser -l o -d")
else:
    print( "Numero de parámetros incorrectos ")

