# 1) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
# In [13]:
# Completa el ejercicio aquí
# resultado = 10/0


# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# <ipython-input-13-fa18751f1091> in <module>()
#       1 # Completa el ejercicio aquí
# ----> 2 resultado = 10/0

# ZeroDivisionError: division by zero

try:
    resultado = 10/0
    print(resultado)
except ZeroDivisionError:
    print("O resultado de unha división entre 0 é unha indterminación matemática.")

    # print("Error: No es posible dividir por cero, debes introducir un número distinto.")