# Definir en python una función maximoDeTres(), que tome tres números 
# como argumentos y devuelva el mayor de ellos. 


def maximo_de_tres(a, b, c):
    if a > b > c:
        print(a , " é o maior.")
    elif b > a > c or b > c > a :
        print(b, " é o maior.")
    elif a < b < c:
        print(c, " é o maior.")
    else:
        print("outra")
    

maximo_de_tres(3,2,1)
maximo_de_tres(1,3,2)
maximo_de_tres(1,2,3)

# Solución de Ángel 
# def maximoDeTres(n1,n2,n3):
#     max = n1
#     if(n2>max):
#         max = n2
#     if(n3>max):
#         max = n3
#     return max
