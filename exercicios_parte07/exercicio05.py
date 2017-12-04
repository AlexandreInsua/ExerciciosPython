# 5) Realiza una función llamada agregar_una_vez() que reciba una lista y un elemento. 
# La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. 
# Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:
#  Error: Imposible añadir elementos duplicados => [elemento].
# Prueba de agregar los elementos 10, -2, "Hola" a la lista de elementos con la función una vez la has creado y luego muestra su contenido.
# Nota: Puedes utilizar la sintaxis: elemento in lista
# In [9]:
# elementos = [1, 5, -2]

def agregar_una_vez(lista, ele):
    try:
        if ele in lista:
            raise ValueError
        else:
            lista.append(ele)
    except:
        print("Non se pode repetir un elemento.")
elementos = [1, 5, -2]
agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
agregar_una_vez(elementos, "Hola")
