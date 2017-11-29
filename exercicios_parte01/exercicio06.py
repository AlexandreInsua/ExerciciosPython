# Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés.
# Al parecer contiene el nombre de un alumno y la nota de un exámen.
#  ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?:
# Nombre Apellido ha sacado un Nota de nota.
# Ayuda: Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]

cadena = "zeréP nauJ,01"
cadena_volteada = cadena[::-1]
print(cadena_volteada)
name = cadena_volteada[3:7]
surname = cadena_volteada[7:]
note = cadena_volteada[0:2]

print("{} {}  ha sacado un {}".format( name, surname, note))