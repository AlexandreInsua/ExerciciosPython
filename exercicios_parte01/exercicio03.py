# El siguiente código pretende realizar una media entre 3 números, pero no funciona
#  correctamente. ¿Eres capaz de identificar el problema y solucionarlo?

numero_1 = 9
numero_2 = 3
numero_3 = 6

# orixinal
media = numero_1 + numero_2 + numero_3 / 3
print("La nota media es", media)  # devolve 14; imposible

# O problema está na prioridade de operadores: primeiro realízase a división e 
# logo as sumas

# corrixido
media = (numero_1 + numero_2 + numero_3) / 3
print("La nota media es", media)  # devolve 6; correcto
