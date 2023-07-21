import sys


def exibir_menu():
    print("Escolha uma opção:")
    print("1 - Cadastrar Aluno")
    print("2 - Remover Aluno")
    print("3 - Editar Aluno")
    print("4 - Listar Aluno")
    print("5 - Sair")


def cadastrar_aluno():
    print("Vai salvar esse aluno, no formato JSON, em um arquivo")
    # Fazer uma exception para verificar se o CPF tem 11 digitos
    # (OPCIONAL) Para bater as paradas: Validar o email, para verficar se é válido
    # (OPCIONAL) Salvar no em um banco de dados simples.


def remover_aluno():
    print("Essa função remove o aluno da lista ou arquivo ou banco de dados")


def editar_aluno():
    print("Editar um aluno da lista")


def listar_alunos():
    print("Vai listar os alunos cadastrados na lista/arquivo/banco")


def fechar_programa():
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
    else:
        # Fazer tratamento de exceção para não deixar número maior que 5 e menor que 1
        fechar_programa()
