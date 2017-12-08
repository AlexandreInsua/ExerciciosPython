# Realiza el juego Piedra - Papel - Tijera con python
# Intenta que sea genérico

# Primera solución:

PIEDRA = 0
PAPEL = 1
TIJERA = 2

p1=PIEDRA
p2=PAPEL

if p1==PIEDRA and p2==PIEDRA:
   print("empate")
elif p1==PIEDRA and p2==PAPEL:
   print("gana p2")
elif p1==PIEDRA and p2==TIJERA:
   print("gana p1")
elif p1==PAPEL and p2==PIEDRA:
   print("gana p1")
elif p1==PAPEL and p2==PAPEL:
   print("empate")
elif p1==PAPEL and p2==TIJERA:
   print("gana p2")
elif p1==TIJERA and p2==PIEDRA:
   print("gana p2")
elif p1==TIJERA and p2==PAPEL:
   print("gana p1")
elif p1==TIJERA and p2==TIJERA:
   print("empate")
# Segun la teoría de combinatoria
# n=cantidad elementos = 3
# k=grupos = 2
# n! / k! * (n-k)!
# 3! / 2! * (3-2)!
# 6 / 2 * 1
# 3 combinaciones posibles


# Segunda solución más genérica
(PIEDRA, PAPEL, TIJERA) = range(3)

reglas = {
   PIEDRA: TIJERA,
   PAPEL: PIEDRA,
   TIJERA: PAPEL
}


def juego(p1, p2):
       print(p1,p2,reglas[p1],reglas[p2])
       if p1 == reglas[p2]:
           print("gana P2")
       elif p2 == reglas[p1]:
           print("gana P1")
       else:
           print("empate")

juego(PIEDRA,PIEDRA)
juego(PIEDRA,PAPEL)
juego(PAPEL,PIEDRA)
juego(TIJERA,PIEDRA)

