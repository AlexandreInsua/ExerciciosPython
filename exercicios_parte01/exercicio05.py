#5) La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, 
# y es que en cada fila, el cuarto elemento siempre debe ser el resultado de sumar los tres primeros.
# ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?
#Ayuda: La función llamada sum(lista) devuelve una suma de todos los elementos de la lista ¡Pruébalo!

# orixinal
matriz = [ 
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

print("Matriz orixinal: ")
for fila in matriz:
    print("\t", fila)

print("\nMatriz modificada")
for fila in matriz:
    fila[3] = sum(fila[:3]) 
    print("\t", fila)

# Ángel usa os slicing desde o final:
# o 4º elemento = suma dos 3 primeiros [:-1] desde o principio até o final, excluído este.
# matriz[1][-1] = sum(matriz[1][:-1])
# matriz[3][-1] = sum(matriz[3][:-1])
