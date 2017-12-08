# Crea un programa (en Python) que pida constantemente por pantalla que le introduzcan frases(texto) 
# o números.
# Cuando el usuario introduzca la palabra fin el programa terminará y mostrará por pantalla
# todas las frases y la suma de todos los números.

# NOTA: usa isnumeric() para saber si es un número o no

# Tendrás que ir guardando las frases(texto) en una lista e ir guardando en una variable suma,
# la suma de todos los números.


frases = []
suma = 0

datos = ""
while(datos.lower() != "fin"):
    datos = input("Introduce una frase o un número:")
    if(datos.isnumeric() ):
        suma += int(datos)
    else:
        if(datos.lower() != "fin"):
            frases.append(datos)    


print("LISTA DE FRASES")
for frase in frases:
    print("- "+frase)
print("LA SUMA DE LOS NÚMEROS VALE: " + str(suma) )

