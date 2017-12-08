# Programa en python (llamado sumar.py) que sume todos los argumentos que se le pasen como parámetro.
# Valida que sean números los argumentos.
# Se podrán sumar números enteros y con comas.
# Ej python  sumar.py 2 5 2
# Resultado: 9

import sys

def esNumerico(num):
    try:
        float(num)
        return True
    except:
        return False


suma = 0
for i in range(1, len(sys.argv) ):
    if( esNumerico (sys.argv[i])  ):
        suma += float( sys.argv[i] )
print( str( suma) )


