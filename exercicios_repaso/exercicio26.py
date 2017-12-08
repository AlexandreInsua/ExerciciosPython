# Crea un programa (en Python) que pida constantemente por pantalla que le introduzcan nombres y apellidos de persona. (se guardarán en una colección)
# Ej:
# Juan Perez Gonzalez
# Ruben Diaz Guzmán
# Rosario María Porto González

# Cuando se inserte el nombre fin (sin importar mayúsculas y minúsculas) se mostrará por pantalla las iniciales de cada una de las personas introducidas.
# Ej:
# JPG
# RDG
# RMPG


def leerPersonas():
    personas=[]
    persona=""
    # pasa todo a minúsculas
    while(persona.lower() != "fin"):
        persona = input("Dame tu nombre y apellidos:")
        if(persona.lower() != "fin"):
            personas.append(persona)
    return personas

def mostrarInicialesDePersonas(listaPersonas):
    for persona in listaPersonas:
        # cuartea persona
        arrayNombre = persona.split(" ")
        temp = ""
        for nombre in arrayNombre:
            temp = temp + nombre[0]
        print(temp)


personas = leerPersonas()

mostrarInicialesDePersonas(personas)
