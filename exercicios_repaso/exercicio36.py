# Supón un diccionario que contiene como llave(clave) el nombre de una persona y 
# como valor una lista con todas sus “gustos”. Desarrolla una función 
# def agregueGusto(diccionario, persona, gusto) tal que:
# * Si la persona no existe la agregue al diccionario con una lista que contiene un solo elemento.
# * Si la persona existe y el gusto existe en su lista, no tiene ningún efecto.
# * Si la persona existe y el gusto no existe en su lista, agrega el gusto a la lista.

def agregarGusto(diccionario, persona, gusto):
    if persona in diccionario: # la persona ya existe en el diccionario
        if not gusto in diccionario[persona] : # añadimos el gusto a la lista de gustos de la persona
            diccionario[persona].append(gusto)
    else: # la persona no existe en el diccionario
        diccionario[persona] = [gusto]

nombresPersona = {}

agregarGusto(nombresPersona, "Maria", "Ropa")
agregarGusto(nombresPersona, "Maria", "Peliculas")
agregarGusto(nombresPersona, "Juan", "Futbol")
agregarGusto(nombresPersona, "Juan", "Futbol")
agregarGusto(nombresPersona, "Tomas", "Futbol")
agregarGusto(nombresPersona, "Tomas", "Informatica")

for clave,valor in nombresPersona.items():
    print(clave )
    for gusto in valor:
        print("  - " + gusto)

