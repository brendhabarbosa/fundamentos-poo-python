class Pessoa(object):
    def __init__(self, nome, idade,email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}"

class Aluno(Pessoa):
    def __init__(self, nome, idade, email, matricula, curso):
        super().__init__(nome, idade, email)
        self.matricula = matricula
        self.curso = curso

    def __str__(self):
            return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}"

    def exibir_dados_aluno(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}, Matrícula: {self.matricula}, Curso: {self.curso}"

object1 = Aluno("Luisa", 20, "luisinha@gmail", "12345", "Engenharia")
print(object1.exibir_dados_aluno())


class Curso(object):
    def __init__(self, nome):
          self.nome = nome
          self.alunos = []
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    def exibir_alunos(self):
        for aluno in self.alunos:
            print(aluno.exibir_dados_aluno())

curso1 = Curso("Engenharia")
aluno1 = Aluno("Luisa", 20, "luisinha@gmail", "12345", "Engenharia")
aluno2 = Aluno("João", 25, "joaogmail.com", "67890", "Engenharia")
curso1.adicionar_aluno(aluno1)
curso1.adicionar_aluno(aluno2)
curso1.exibir_alunos()

