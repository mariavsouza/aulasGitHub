from sql import *
from funcoes import *
from validacoes import *

def menu():
    while True:
        print("\n --- MENU ---")
        print("1 - Cadastrar aluno;")
        print("0 - Sair")
 
        opcao = input("\nEscolha uma opção: ")
 
        if opcao == "1":
            cadastrar_aluno()
        if opcao == "0":
            print("Encerrando sistema...")
            break
        else: 
            print("Opção invalida!")

menu()