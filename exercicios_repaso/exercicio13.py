# Ejercicio 13:
# Crea un fichero de texto lleno de números (positivos y negativos) separados por puntos y comas.
# Crea un programa en python que lea ese fichero y sume todos los números, pero descartando los números que sean negativos.



#abrimos el fichero en modo lectura
fichero = open("numeros.txt", "r")
#leemos todos su contenido
numeros = fichero.read()
#usamos un acumulador para ir guardando la suma
suma = 0
#trocemos la cadena de texto para quedarnos solo con
#los numeros (en formato string)
numerosSeparado = numeros.split(";")
#recorremos todos los numeros
for i in numerosSeparado:
    #convertimos el numero(texto) a numero(entero)
    valor = int(i)
    #solo si el numero es positivo los añado al acumulador
    if(valor>0):
        suma = suma + valor

#cerramos el fichero
fichero.close();
#pintamos la suma en pantalla
print(suma)