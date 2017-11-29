# 3) Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:
# Guarda en una variable numero_magico el valor 12345679 (sin el 8)
# Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9 (asegúrate que es un número)
# Multiplica el numero_usuario por 9 en sí mismo
# Multiplica el numero_magico por el numero_usuario en sí mismo
# Finalmente muestra el valor final del numero_magico por pantalla

numero_magico = 123245679
print("Presentamos o número máxico.")
numero_usuario = int(input("Introduza un número entre 1 e 9: "))
if 0 < numero_usuario <10:
    numero_usuario = numero_usuario * 9
    numero_magico = numero_magico * numero_usuario
    print(numero_magico)
else:
    print("O numero debe ser entre 1 e 9 ambos incluídos.")