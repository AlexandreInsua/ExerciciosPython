class Usuario:
    # atributos
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


