
# Programa que acepte por parámetros de consola 2 números enteros (base y exponente) y 
# calcule base elevado a exponente.
# Ej exponente 2 8
# Resultado= 256
# Nota: Valida que los datos sean correctamente pasados.


import sys

#print("numero de parametros" + str( len(sys.argv) ) )
#print("parametros:"+ str( sys.argv ) )
#print("Primer parametro(nombre del programa): "+sys.argv[0] )
#print("Segundo parámetro: "+sys.argv[1] )

if len(sys.argv != 3 ):
    print("Error tienes que pasar 2 argumentos (base y exponente)")
    exit()

texto = sys.argv[1]
if not texto.isnumeric():
    print("Error, la base tiene que ser un número")
    exit()
base = int(texto)

texto = sys.argv[2]
if not texto.isnumeric():
    print("Error, el exponente tiene que ser un número")
    exit()
exponente = int(texto)

resultado = base ** exponente

print(resultado)
