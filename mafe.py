#importações de recursos externos
import mysql.connector
from mysql.connector import Error
from datetime import datetime

#listas pré estabelecidas | colocar as materias em determinadas turmas
alunos = []
professores = []
turma = []
notas = []
materias = ["português", "inglês", "artes", 
            "educação física", "matemática", "geografia", 
            "história", "sociologia", "filosofia", "biologia", 
            "química", "física", "projeto de vida",]


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
def validar_nome(nome):
    if not nome.strip():
        print("O nome não pode estar vazio.")
        return False
 
    if not all(parte.isalpha() for parte in nome.replace(" ", "").split()):
        print("O nome deve conter apenas letras.")
        return False
 
    return True


def validar_nascimento(data_nascimento):
    try:
        data = datetime.strptime(data_nascimento, "%d/%m/%Y")
 
        if data > datetime.now():
            print("A data de nascimento não pode ser futura.")
            return False
 
        return True
 
    except ValueError:
        print("Formato inválido. Use DD/MM/AAAA.")
        return False
 

def validar_turma(turma):
    if not turma.strip():
        print("A turma não pode estar vazia.")
        return False
 
    return True


def validar_notas(notas):
    if not isinstance(notas, list):
        print("As notas devem ser uma lista.")
        return False
 
    for nota in notas:
        if not isinstance(nota, (int, float)):
            print("Todas as notas devem ser numéricas.")
            return False
 
        if nota < 0 or nota > 10:
            print("As notas devem estar entre 0 e 10.")
            return False
 
    return True

def validar_materia():
    ...

#defs funções
def mostrar_materias(turma):

    if turma not in materias:
        print("Turma não encontrada")
        return

    print(f"\nMatérias da turma {turma}:\n")

    for materia in materias[turma]:
        print("-", materia)


mostrar_materias("1A")

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    
    if not validar_nome(nome):
        return 
        
    data_nascimento = input("Data de Nascimento: ")
    
    if not validar_nascimento(data_nascimento):
        return 

    turma = input("Turma: ")
    
    if not validar_turma(turma):
        return 

    dados = [nome, data_nascimento, turma, notas]
    alunos.append(dados)

    print("Aluno cadastrado com sucesso!")


def cadastrar_prof():
    nome = input("Nome do Professor: ")
    
    if not validar_nome(nome):
        return 

    turma = input("Turma: ")

    if turma not in materias:
        print("Turma inválida.")
        return

    print("\nMatérias disponíveis:")
    
    for materia in materias[turma]:
        print("-", materia)

    materia = input("\nEscolha a matéria: ")

    if not validar_materia(turma, materia):
        return 

    dadosprof = [nome, materia]
    professores.append(dadosprof)

    print("Professor cadastrado com sucesso!")


def cadastrar_turma():
    ...

def adicionar_nota():
    ...

def editar_nota():
    ...

def editar_alunos():
    ...

def editar_prof():
    ...

def remover_nota():
    ...

def remover_aluno():
    ...

def remover_prof():
    ...

def remover_turma():
    ...

def parecer_aluno():
    ...

#menus #COMPLETOS
def menu_aluno():
    while True:
        print("\n --- MENU DE AÇÕES DO ALUNO\\RESPONSÁVEL ---")
        print("1 - Visualizar parecer do aluno")
        print("0 - Sair do Sistema")
        actAluno = input("\nO que você deseja fazer: ")

        if actAluno == "1":
            return parecer_aluno()
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
            return adicionar_nota()
        elif actProf == "2":
            return remover_nota()
        elif actProf == "3":
            return editar_nota()
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
            return remover_aluno()
        elif actSecre == "3":
            return cadastrar_prof()
        elif actSecre == "4":
            return remover_prof()
        elif actSecre == "5":
            return cadastrar_turma()
        elif actSecre == "6":
            return remover_turma()
        elif actSecre == "7":
            return editar_alunos()
        elif actSecre == "8":
            return editar_prof()
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