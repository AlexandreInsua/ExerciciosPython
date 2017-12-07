#  A partir del ejercicio anterior, vamos a suponer que cada número es una nota,
#  y lo que queremos es obtener la nota media. El problema es que cada nota tiene un valor porcentual:
# La primera nota vale un 15% del total
# La segunda nota vale un 35% del total
# La tercera nota vale un 50% del total
# Desarrolla un programa para calcular perfectamente la nota final.

nota_1 = 10
nota_2 = 7
nota_3 = 4

media = (nota_1 + nota_2 + nota_3) / 3
media_ponderada = nota_1 * 0.15 + nota_2 * 0.35 + nota_3 * 0.50 

print("A nota media é: ", media )
print("A nota media ponderada é  {:.2f}".format(media_ponderada))