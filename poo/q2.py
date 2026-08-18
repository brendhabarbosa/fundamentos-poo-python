class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"
    def check_idade(self):
        if self.idade < 1:
            return "Idade inválida"
        return f"A idade {self.idade} é válida"
    def birthday(self):
        self.idade +=1
        return f"{self.nome} agora tem {self.idade} anos"

object1 = Pessoa("Luisa", 20)
object2 = Pessoa("Luis", 0)

print(object1.birthday())
print(object2.check_idade()) 
