# 6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:
# Por ejemplo:
# pares, impares = separar([6,5,2,1,7])
# print(pares)   # valdría [2, 6]
# print(impares)  # valdría [1, 5, 7]

# Nota: Para ordenar una lista automáticamente puedes usar el método .sort().

numeros = [-12, 84, 13, 20, -33, 101, 9]

def separar(lista):
    numeros.sort()
    pares = []
    impares = []

    for i in numeros:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

# método que devolve dúas listas
pares, impares = separar(numeros)
print(pares)
print(impares)

