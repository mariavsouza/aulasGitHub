#importações de recursos externos
import mysql.connector
from mysql.connector import Error

#listas pré estabelecidas
alunos = []
professores = []
notas = []

#conexão com mySQL (sem conexão nas defs ainda)
def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Senac2026',
            database='sistemaEscolar'
        )
        return conexao
 
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
    
#validações
def validar_nome():
    ...

def validar_nascimento():
    ...

def validar_turma():
    ...

def validar_notsa():
    ...

def validar_materia():
    ...

#funções
def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    
    data_nascimento = input("Data de Nascimento: ")

    turma = input("Turma: ")

    dados = [nome, data_nascimento, turma, notas]
    alunos.append(dados)
    print("Aluno Cadastrado!")

def cadastrar_prof():
    nome = input("Nome do Professor: ")

    materia = input("Matéria Lecionada: ")

    dadosprof = [nome, materia]
    professores.append(dadosprof)
    print("Professor Cadastrado!")
#menus
def menu_aluno():
    while True:
        print("\n --- MENU DE AÇÕES DO ALUNO\\RESPONSÁVEL ---")
        print("1 - Visualizar parecer do aluno")
        print("0 - Sair do Sistema")
        actAluno = input("\nO que você deseja fazer: ")

        if actAluno == "1":
            ...
        elif actAluno == "0":
            print("\nVocê saiu do Sistema Instituto D'Souza. Encerando serviços...")
            break
        else:
            print(">>ERRO<<\nEscolha uma opção válida mostrada acima!")
            continue
    
def menu_professor():
    while True:
        print("\n --- MENU DE AÇÕES DO PROFESSOR ---")
        print("1 - Adicionar Notas")
        print("2 - Remover Notas")
        print("3 - Editar Notas")
        print("0 - Sair do Sistema ")
        actProf = input("\nO que você deseja fazer: ")

        if actProf == "1":
            ...
        elif actProf == "2":
            ...
        elif actProf == "3":
            ...
        elif actProf == "0":
            print("\nVocê saiu do Sistema Instituto D'Souza. Encerando serviços...")
            break
        else:
            print(">>ERRO<<\nEscolha uma opção válida mostrada acima!")
            continue
        
def menu_secretario():
     while True:
        print("\n --- MENU DE AÇÕES DO SECRETÁRIO---")
        print("1 - Cadastrar Aluno")
        print("2 - Remover Aluno")
        print("3 - Cadastrar Professor")
        print("4 - Remover Professor")
        print("5  - Cadastrar Turma")
        print("6 - Remover Turma")
        print("7 - Editar Dados dos Aluno")
        print("8 - Editar Dados do Professor")
        print("0 - Sair do Sistema ")
        actSecre = input("\nO que você deseja fazer: ")

        if actSecre == "1":
            return cadastrar_aluno()
        elif actSecre == "2":
            ...
        elif actSecre == "3":
            ...
        elif actSecre == "4":
            ...
        elif actSecre == "5":
            ...
        elif actSecre == "6":
            ...
        elif actSecre == "7":
            ...
        elif actSecre == "8":
            ...
        elif actSecre == "0":
            print("\nVocê saiu do Sistema Instituto D'Souza. Encerando serviços...")
            break
        else:
            print(">>ERRO<<\nEscolha uma opção válida mostrada acima!")
            continue

def menu_inicial():
    print("\n----- Bem vindo ao sistema do Instituto D'Souza -----")
    while True:  
        print("\n --- OPÇÕES DE LOGIN ---")
        print("1 - Aluno\\Responsável")
        print("2 - Professor(a)")
        print("3 - Secretário")
        print("0 - Sair do Sistema")
        login = input("\nQual a sua forma de login?: ")

        if login == "1":
            return menu_aluno()
        elif login == "2":
            return menu_professor()
        elif login == "3":
            return menu_secretario()
        elif login == "0":
            print("\nVocê saiu do Sistema Instituto D'Souza. Encerando serviços...")
            break
        else:
            print(">>ERRO<<\nEscolha uma opção válida mostrada acima!")
            return

menu_inicial()