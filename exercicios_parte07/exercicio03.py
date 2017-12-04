# 3) Localiza el error en el siguiente bloque de código.
#  Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
# In [11]:
# Completa el ejercicio aquí
# colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
# colores['blanco']


# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# <ipython-input-11-9316804f855a> in <module>()
#       1 # Completa el ejercicio aquí
#       2 colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
# ----> 3 colores['blanco']

# KeyError: 'blanco'
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
try:
    colores['blanco']
except KeyError:
    print("A clave non existe.")