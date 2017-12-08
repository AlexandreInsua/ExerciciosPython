
# Escribir en python una función suma() y una función resta() que sumen y resten respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y resta([9,1,1]) debería devolver 7.


def suma(lista):
    suma = 0
    for n in lista:
        suma += n
    print(suma)

def resta(lista):
    resta = lista[0] * 2
    for n in lista:
        resta -= n
    print(resta)



lista1 = [1,2,3,4]
lista2 = [9,1,1]

suma(lista1)
resta(lista2)