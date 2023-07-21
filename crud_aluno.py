import sys

alunos = []


def exibir_menu():
    print("Escolha uma opção:")
    print("1 - Cadastrar aluno(a)")
    print("2 - Remover aluno(a)")
    print("3 - Editar aluno(a)")
    print("4 - Listar alunos")
    print("5 - Sair")


def cadastrar_aluno():
    print("Digite o nome do aluno:")
    nome = input()
    print("Digite o CPF do aluno:")
    cpf = input()
    try:
        if len(cpf) != 11:
            raise ValueError("O CPF deve ter 11 dígitos.")
        int(cpf)  # Verifica se o CPF é composto apenas por dígitos numéricos
    except ValueError as e:
        print(e)
        return
    print("Digite o e-mail do aluno:")
    email = input()
    print("Digite o telefone do aluno:")
    telefone = input()
    alunos.append({"nome": nome, "cpf": cpf, "email": email, "telefone": telefone})
    print("Aluno cadastrado com sucesso!")


def remover_aluno():
    print("Digite o nome do aluno que deseja remover:")
    nome = input()
    for aluno in alunos:
        if aluno["nome"] == nome:
            alunos.remove(aluno)
            print("Aluno removido com sucesso!")
            break
    else:
        print("Aluno não encontrado.")


def editar_aluno():
    print("Digite o nome do aluno que deseja editar:")
    nome = input()
    for aluno in alunos:
        if aluno["nome"] == nome:
            print("Escolha uma opção para editar:")
            print("1 - Nome")
            print("2 - CPF")
            print("3 - E-mail")
            print("4 - Telefone")
            opcao = input()
            if opcao == "1":
                print("Digite o novo nome do aluno:")
                aluno["nome"] = input()
            elif opcao == "2":
                print("Digite o novo CPF do aluno:")
                aluno["cpf"] = input()
            elif opcao == "3":
                print("Digite o novo e-mail do aluno:")
                aluno["email"] = input()
            elif opcao == "4":
                print("Digite o novo telefone do aluno:")
                aluno["telefone"] = input()
            print("Aluno editado com sucesso!")
            break
    else:
        print("Aluno não encontrado.")


def listar_alunos():
    print("Lista de alunos:")
    for aluno in alunos:
        print("Nome:", aluno["nome"])
        print("CPF:", aluno["cpf"])
        print("E-mail:", aluno["email"])
        print("Telefone:", aluno["telefone"])


def sair():
    sys.exit()


while True:
    exibir_menu()
    escolha = input()
    if escolha == "1":
        cadastrar_aluno()
    elif escolha == "2":
        remover_aluno()
    elif escolha == "3":
        editar_aluno()
    elif escolha == "4":
        listar_alunos()
    elif escolha == "5":
        sair()
    else:
        print("Opção inválida.")
