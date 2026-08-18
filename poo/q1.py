class Pessoa(object):
    def __init__(self, nome, idade,email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}"

object1 = print(Pessoa("Luisa", 20, "luisinha@gamil.com"))
object2 = print(Pessoa("João", 25, "joaogmail.com"))
object3 = print(Pessoa("Maria", 30, "maria@hotmail.com"))