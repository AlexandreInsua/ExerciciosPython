# Realiza una función en python a la que le pases como parámetro una tupla de números y un entero x. La función devolverá el total de números que son mayores que x.

def maximoDe(miTupla, numero):
    contador = 0
    for i in miTupla:
        if i > numero:
            contador = contador + 1
    return contador



#lista = [2,5,2,6]
miTupla = (3,6,23,8,9,4)

print ( maximoDe(miTupla, 5) )