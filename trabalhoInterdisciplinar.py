def validar_dados():
    ...
    
def cadastrar_aluno():
    ...

def listar_aluno():
    ...

def remover_aluno():
    ...

def editar_dados():
    ...

def adicionar_notas():
    ...

def remover_notas():
    ...

def caucular_media():
    ...

def situção_aluno():
    ...

def buscar_aluno():
    ...


def menu():
    while True:
        print("\n --MENU--")
        print("1 - Cadastrar aluno;")
        print("2 - Listar aluno;")
        print("3 - Remover aluno;")
        print("4 - Editar dados do aluno;")
        print("5 - Adicionar notas;")
        print("6 - Remover notas;")
        print("7 - Caucular media do aluno;")
        print("8 - Situação do aluno;")
        print("9 - Buscar por aluno;")
        print("0 - Sair")
 
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_aluno()

        elif opcao == "3":
            remover_aluno()

        elif opcao == "4":
            editar_dados()

        elif opcao == "5":
            adicionar_notas()

        elif opcao == "6":
            remover_notas()

        elif opcao == "7":
            caucular_media()

        elif opcao == "8":
            situção_aluno()

        elif opcao == "9":
            buscar_aluno()

        elif opcao == "0":
            print("você saiu do Sistema do Instituto D'Souza")
            break

        else:
            print("Opção inválida!")

print("Bem vindo ao sistema do Instituto D'Souza")
menu()