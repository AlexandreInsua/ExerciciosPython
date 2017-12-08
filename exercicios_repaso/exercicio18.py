# Realiza una función en python que tome como parámetro una lista de textos.
# Nos devolverá el texto que sea más largo.


def  bigger_string(listaTextos):
    if(len(listaTextos) == 0):
        return 0
    max = listaTextos[0]
    for i in listaTextos:
        if(len(i) > len(max)):
            max = i
    return max

# extra de Ángel
def bigger_index(listaTextos):
    if(len(listaTextos) == 0):
        return -1
    indiceMayor = 0
    contador = 0
    for i in listaTextos:
        if(len(i) > len(listaTextos[indiceMayor])):
            indiceMayor = contador
        contador = contador + 1
    return indiceMayor

lista = ["antonio","angel", "bea", "pepe","antonio"]

mayor = bigger_string(lista)
print(mayor)

mayor = bigger_index(lista)
print(mayor)
