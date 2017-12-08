# Crea una clase (en python) llamada Usuario.
# Tendrá por atributos: nombre, apellido1, apellido2, teléfono, email y dirección.
# Tendrá un constructor
# Tendrá un método __str__ para mostrar los datos del usuario por pantalla
# Tendrá otro método llamado nombreCompleto, que devolverá el nombre y apellidos concatenados 
# y en mayúscula.
# Tendrá otro método llamado prefijoTelefónico, que devolverá los 3 primeros caracteres del teléfono.
# Usar un poco la clase a modo de ejemplo.


class Usuario:
    # atributos non é necesario declaralos.
    nome = ""
    apelido1 = ""
    apelido2 = ""
    telefono = ""
    email = ""
    direccion = ""

    # construtor
    def __init__(self, nome, apelido1, apelido2, telefono, email, direccion):
        self.nome = nome
        self.apelido1 = apelido1
        self.apelido2 = apelido2
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
    
    # to strign
    def __str__(self):
        return "{}{}{}{}{}{}".format(self.nome, self.apelido1, self.apelido2, self.telefono, self.email, self.direccion)
    
    def nomeCompleto(self):
        nome_completo = self.nome + " " + self.apelido1 + " " +self.apelido2
        return nome_completo.capitalize()

    def prefixoTelefonico(self):
        prex = self.telefono[:3]
        return prex


u = Usuario("roi", "batti", "nexus 6", "555-939-923-933", "replicante03@hotmail.com", "Tyrell Co s/n")

print(u.__str__())
print(u.nomeCompleto())
print(u.prefixoTelefonico())

u = Usuario("Angel", "Gonzalez", "Martinez","986472211",
    "gonzalezm.angel@gmal.com", "Pizarro")
print(u)
print(u.nomeCompleto())
print(u.prefixoTelefonico())