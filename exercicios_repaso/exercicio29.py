
# Ejercicio 29
# Crea un programa en python que sirva para convertir monedas.

# * Primero pedirá (mediante un menú) que se indique el tipo de divisa inicial que vas a usar (ej: dólar, euro, libra, …)
# * Luego pedirá un valor numérico por pantalla (float), que será la cantidad de esa divisa.
# * Por último se pedirá (mediante un menú) a qué tipo de divisa deseas convertir. ej(a dólares, euros, libras, …)
#  Nota: si se eligió como tipo de divisa inicial el euro, no te pedirá que la conviertas a euros (no tiene sentido)


def calcularConversion(tipoDivisaOrigen, cantidad, tipoDivisaDestino):
    if(tipoDivisaOrigen == 1): #euro
        if(tipoDivisaDestino == 1): #euro
            return cantidad
        elif(tipoDivisaDestino == 2): #dolar
            return cantidad*1.124
        elif(tipoDivisaDestino == 3): # libras
            return cantidad*0.87
        else: #error
            return -1
    elif(tipoDivisaOrigen == 2): #dolar
        if(tipoDivisaDestino == 1): #euro
            return cantidad*0.89
        elif(tipoDivisaDestino == 2): #dolar
            return cantidad
        elif(tipoDivisaDestino == 3): # libras
            return cantidad*0.77
        else: #error
            return -1
    elif(tipoDivisaOrigen  == 3): # libra
        if(tipoDivisaDestino == 1): #euro
            return cantidad*1.15
        elif(tipoDivisaDestino == 2): #dolar
            return cantidad*1.30
        elif(tipoDivisaDestino == 3): # libras
            return cantidad
        else: #error
            return -1
    else: # error
        return -1


print("Selecciona la divisa de origin")
print("1- Euro")
print("2- Dolar")
print("3- Libra")
print("4- Salir")

tipoDivisaOrigen = int(input("Seleccina opción:"))

if(tipoDivisaOrigen == 4):
    exit()
cantidad = float(input("Cantidad de esa divisa:"))

print("Selecciona la divisa a la cual convertir")

if(tipoDivisaOrigen != 1):
    print("1- Euro")
if(tipoDivisaOrigen != 2):
    print("2- Dolar")
if(tipoDivisaOrigen != 3):
    print("3- Libra")
print("4- Salir")


tipoDivisaDestino = int(input("Seleccina opción:"))
if(tipoDivisaDestino == 4):
    exit()

resultado = calcularConversion(tipoDivisaOrigen, cantidad, tipoDivisaDestino)
print(resultado)
