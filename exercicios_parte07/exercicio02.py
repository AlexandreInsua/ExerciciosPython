# 2) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee
# y además explica en un mensaje al usuario la causa y/o solución:
# In [14]:
# Completa el ejercicio aquí
# lista = [1, 2, 3, 4, 5]
# lista[10]


# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-14-04f772275640> in <module>()
#       1 # Completa el ejercicio aquí
#       2 lista = [1, 2, 3, 4, 5]
# ----> 3 lista[10]

# IndexError: list index out of range

lista = [1, 2, 3, 4, 5]
try:
    lista[10]
except IndexError:
    print("Unha sentenza sobrepasa o da lista")