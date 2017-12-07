# 4) Localiza el error en el siguiente bloque de código. 
# Crea una excepción para evitar que el programa se bloquee y 
# además explica en un mensaje al usuario la causa y/o solución:
# In [10]:
# Completa el ejercicio aquí
# resultado = 15 + "20"

# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-10-4c554866ea5f> in <module>()
#      1 # Completa el ejercicio aquí
# ----> 2 resultado = 15 + "20"

# TypeError: unsupported operand type(s) for +: 'int' and 'str'

try:
    resultado = 15 + "20"
except TypeError:
    print("Os operadores son de tipo diferente e non e poder realizar a operación.")

# print("Error: Sólo es posible sumar datos del mismo tipo, debes transformar el 
# número a cadena o la cadena a número.")