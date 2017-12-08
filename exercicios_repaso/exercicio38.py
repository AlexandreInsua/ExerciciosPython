# Guarda en una colección de tipo lista 1000 números aleatorios.
# Guarda esa lista en un fichero de texto llamado lista.txt, separa los números por el símbolo ;
# Lee la lista (lista.txt) guardada en el disco duro, eleva al cuadrado los números y guardalos en una colección tipo lista.


from random import randint
#creamos una lista vacia
listaNumeros=[]

#recorro un bucle de 1000 ciclos
for numero in range(1,1001):
    #genero un número aleatorio
    aleatorio = randint(0,9)
    #añado el numero aleatorio a la lista
    listaNumeros.append(aleatorio)

#abro un fichero en modo escritura
fichero = open("lista.txt", "w")
#recorro la lista
for numero in listaNumeros:
    #escribo en el fichero ese número seguido de un separador ;
    fichero.write( str(numero) + ";" )

#cierro el fichero
fichero.close()


#abro de nuevo el fichero en modo lectura
fichero2 = open("lista.txt", "r")
#leo todo el contenido del fichero
datos = fichero2.read()
# cerramos el fichero
fichero2.close();

#separo el contendo a partir de el separador ;
#obtendré una lista de números
numeros = datos.split(";")

listaCuadrado=[]
for n in range(0,len(listaNumeros)):
   try:
       listaCuadrado.append( int(listaNumeros[n])**2  )
   except ValueError:
       pass

print(listaCuadrado)
