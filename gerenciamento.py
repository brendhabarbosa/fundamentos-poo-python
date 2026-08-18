from poo.heranca import Aluno, Curso

print("Sistema de Gerenciamento de Alunos/Cursos")
cursos = []
while True:
    print("\nMenu:")
    print("1. Adicionar curso")
    print("2. Adicionar aluno a um curso")
    print("3. Exibir alunos de um curso")
    print("0. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome_curso = input("Digite o nome do curso: ")
        curso = Curso(nome_curso)
        cursos.append(curso)
        print(f"Curso '{nome_curso}' adicionado com sucesso!")

    elif opcao == 2:
        curso_desejado = input("Digite o nome do curso para adicionar o aluno: ")
        curso_encontrado = None
        for curso in cursos:
            if curso.nome == curso_desejado:
                curso_encontrado = True
                break
        if curso_encontrado:
            nome_aluno = input("Digite o nome do aluno: ")
            idade_aluno = int(input("Digite a idade do aluno: "))
            email_aluno = input("Digite o email do aluno: ")
            matricula_aluno = input("Digite a matrícula do aluno: ")
            curso_aluno = curso_desejado
            aluno = Aluno(nome_aluno, idade_aluno, email_aluno, matricula_aluno, curso_aluno)
            curso.adicionar_aluno(aluno)
            print(f"Aluno '{nome_aluno}' adicionado ao curso '{curso_desejado}' com sucesso!")
        else:
            print(f"Curso '{curso_desejado}' não encontrado.")
    elif opcao == 3:
        curso_desejado = input("Digite o nome do curso para exibir os alunos: ")
        curso_encontrado = None
        for curso in cursos:
            if curso.nome == curso_desejado:
                curso_encontrado = True
                break
        if curso_encontrado:
            print(f"Alunos do curso '{curso_desejado}':")
            curso.exibir_alunos()
        else:
            print(f"Curso '{curso_desejado}' não encontrado.")
    elif opcao == 0:
        print("Saindo do sistema...")
        break