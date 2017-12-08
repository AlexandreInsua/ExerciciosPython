# Realiza una función en python que se le pase como parámetro una lista de números.
# Esta función nos devolverá el mayor de esos números. Llama a la función mayor.

def bigger(lista):
    print(max(lista))

lista = [1, 2, 3, 4, 5]

bigger(lista)

# Ángel filtra a lista:
# def mayor(listaNumeros):
#     #veo si la lista existe
#     if listaNumeros == None:
#         return 0
#     #veo si la lista tiene elementos
#     if len(listaNumeros) == 0:
#          return 0
#     #parto de la suposición de que el mayor de la lista es el primero
#     max = listaNumeros[0]
#     #recorro todos los elementos de la lista
#     for i in listaNumeros:
#         #si el elemento leido es mayor que el máximo, ese elemeneto
#         #leido será el maximo
#         if(i > max):
#             max = i
#     return max

# lista = [2,56,3,10]
# m = mayor(lista)
# print(m)

