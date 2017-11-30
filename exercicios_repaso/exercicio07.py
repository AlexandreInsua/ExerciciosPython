# Programa que le no ficheiro e crea tantos obxectos como for necesario
# Enche o seu nome  engader ao seu array os mensaxes que corresponda

class User:
    def __init__ (self, name, messagesArray):
        self.name = name
        self.messagesArray = messagesArray

# Métodos para realizar as operacións
# Devolve se o usuario está dentre da lista
def seekInList(name, usersList):
    # percorre a lista
    for u in usersList:
        # Se o nome está lista, devólveo
        if (u.name == name):
            return u
    # se non encontra nada, retorna nulto
    return None

# lista de usuarios
usersList = []
# abrimos o ficheiro
file = open("mensajes.txt", "r")
# lemos as liñas
lines = file.readlines()
print(lines)
# percorremos cada unha das liñas do ficheiro
for line in lines:
    # sepearamos o nome da mensaxe
    # o dato será un array de dous elementos
    date = line.split("=")
    name = date[0]
    message = date[1]
    user = seekInList(name, usersList)
    # no caso de non estar na lista
    if (user == None):
        messagesList = []
        messagesList.append(message)
        newUser = User(name, messagesList)
        usersList.append(newUser)
    # se está na lista
    else:
        user.messagesArray.append(message)

# Mostramos en pantalla o resultado
for u in usersList:
    print("Mensaxes de " + u.name)
    for m in u.messagesArray:
        print(" " + m)
