# Realiza el juego Piedra - Papel - Tijera - Lagarto - Spock con python
# Intenta que sea genérico


(PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK) = range(5)
# Reglas del juego. Se usará de la siguiente forma:
# objeto:  objetos a los que gana
reglas = {
   PIEDRA: [LAGARTO, TIJERA],
   PAPEL: [PIEDRA, SPOCK],
   TIJERA: [PAPEL, LAGARTO],
   LAGARTO: [PAPEL, SPOCK],
   SPOCK: [TIJERA, PIEDRA]
}
# Segun la teoría de combinatoria
# n=cantidad elementos = 5
# k=grupos = 2
# n! / k! * (n-k)!
# 5! / 2! * (5-2)!
# 120 / 2 * 3!
# 120 / 2 * 6
# 10 combinaciones posibles

def juego(p1, p2):
       print(p1,p2,reglas[p1],reglas[p2])
       if p1 in reglas[p2]:
           print("gana P2")
       elif p2 in reglas[p1]:
           print("gana P1")
       else:
           print("empate")

juego(PIEDRA,PIEDRA)
juego(PIEDRA,PAPEL)
juego(PAPEL,PIEDRA)
juego(TIJERA,PIEDRA)
juego(LAGARTO,SPOCK)
