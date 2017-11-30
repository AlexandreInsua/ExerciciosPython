# 7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas,
# pero no debe repetirse ningún elemento en la nueva lista (inventa tu las listas):

print("~~ Comparando listas ~~")
lista1 = [20, 1, 4, 11, 19, 16, 12, 3, 5, 14]
lista2 = [1, 12, 5, 11, 6, 2, 13, 17, 19, 3]
lista3 = []

for n in lista1:
    if n in lista2:
        lista3.append(n)

print("lista 1: ",lista1)
print("lista 2: ",lista2)

# extra
lista1.sort()
lista2.sort()
lista3.sort()

print("lista de elementos comúns: ",lista3)