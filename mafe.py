#importações de recursos externos
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from colorama import Fore, init
init()

#listas pré estabelecidas | colocar as materias em determinadas turmas
alunos = []
professores = []
materias = {
    "1EM": [
        "português", "inglês", "artes", "educação física",
        "matemática", "geografia", "história", "sociologia",
        "filosofia", "biologia", "química", "física",
        "projeto de vida"
    ],
    "2EM": [
        "português", "inglês", "artes", "educação física",
        "matemática", "geografia", "história", "sociologia",
        "filosofia", "biologia", "química", "física",
        "projeto de vida"
    ],
    "3EM": [
        "português", "inglês", "artes", "educação física",
        "matemática", "geografia", "história", "sociologia",
        "filosofia", "biologia", "química", "física",
        "projeto de vida"
    ]
}

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

def validar_materia(turma, materia):

    if turma not in materias:
        print("Turma não encontrada.")
        return False

    if materia.lower() not in materias[turma]:
        print("Matéria inválida.")
        return False

    return True

#defs funções
def mostrar_materias(turma):

    if turma not in materias:
        print("Turma não encontrada")
        return

    print(f"\nMatérias da turma {turma}:\n")

    for materia in materias[turma]:
        print("-", materia)

def cadastrar_aluno():

    nome = input("Nome do aluno: ")

    if not validar_nome(nome):
        return

    data_nascimento = input("Data de Nascimento: ")

    if not validar_nascimento(data_nascimento):
        return

    turma = input("Turma (1EM, 2EM ou 3EM): ")

    if turma not in materias:
        print("Turma inválida.")
        return

    aluno = {
        "nome": nome,
        "nascimento": data_nascimento,
        "turma": turma,
        "notas": {}
    }

    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!")

def cadastrar_prof():

    nome = input("Nome do Professor: ")

    if not validar_nome(nome):
        return

    turma = input("Turma (1EM, 2EM ou 3EM): ")

    if turma not in materias:
        print("Turma inválida.")
        return

    print("\nMatérias disponíveis:")

    for materia in materias[turma]:
        print("-", materia)

    materia = input("\nEscolha a matéria: ").lower()

    if materia not in materias[turma]:
        print("Matéria inválida.")
        return

    professor = {
        "nome": nome,
        "turma": turma,
        "materia": materia
    }

    professores.append(professor)

    print("Professor cadastrado com sucesso!")

def cadastrar_turma():

    nome_turma = input("Digite o nome da turma: ")

    if nome_turma in materias:
        print("Turma já cadastrada.")
        return

    materias[nome_turma] = [
        "português",
        "inglês",
        "artes",
        "educação física",
        "matemática",
        "geografia",
        "história",
        "sociologia",
        "filosofia",
        "biologia",
        "química",
        "física",
        "projeto de vida"
    ]

    print("Turma cadastrada com sucesso!")

def adicionar_nota():

    nome = input("Nome do aluno: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            materia = input("Matéria: ").lower()

            if not validar_materia(aluno["turma"], materia):
                return

            nota = float(input("Nota: "))

            if nota < 0 or nota > 10:
                print("Nota inválida.")
                return

            aluno["notas"][materia] = nota

            print("Nota adicionada com sucesso!")
            return

    print("Aluno não encontrado.")

def editar_nota():

    nome = input("Nome do aluno: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            materia = input("Matéria: ").lower()

            if materia in aluno["notas"]:

                nova_nota = float(input("Nova nota: "))

                aluno["notas"][materia] = nova_nota

                print("Nota atualizada!")

            else:
                print("Matéria não encontrada.")

            return

    print("Aluno não encontrado.")

def editar_alunos():

    nome = input("Nome do aluno: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            print("1 - Nome")
            print("2 - Data de Nascimento")
            print("3 - Turma")

            opcao = input("Escolha: ")

            if opcao == "1":
                aluno["nome"] = input("Novo nome: ")

            elif opcao == "2":
                aluno["nascimento"] = input("Nova data: ")

            elif opcao == "3":
                aluno["turma"] = input("Nova turma: ")

            print("Aluno atualizado!")
            return

    print("Aluno não encontrado.")

def editar_prof():

    nome = input("Nome do professor: ")

    for professor in professores:

        if professor["nome"].lower() == nome.lower():

            print("1 - Nome")
            print("2 - Turma")
            print("3 - Matéria")

            opcao = input("Escolha: ")

            if opcao == "1":
                professor["nome"] = input("Novo nome: ")

            elif opcao == "2":
                professor["turma"] = input("Nova turma: ")

            elif opcao == "3":
                professor["materia"] = input("Nova matéria: ")

            print("Professor atualizado!")
            return

    print("Professor não encontrado.")

def remover_nota():

    nome = input("Nome do aluno: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            materia = input("Matéria: ").lower()

            if materia in aluno["notas"]:

                del aluno["notas"][materia]

                print("Nota removida!")

            else:
                print("Matéria não encontrada.")

            return

    print("Aluno não encontrado.")

def remover_aluno():

    nome = input("Nome do aluno: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            alunos.remove(aluno)

            print("Aluno removido!")
            return

    print("Aluno não encontrado.")

def remover_prof():

    nome = input("Nome do professor: ")

    for professor in professores:

        if professor["nome"].lower() == nome.lower():

            professores.remove(professor)

            print("Professor removido!")
            return

    print("Professor não encontrado.")

def remover_turma():

    nome_turma = input("Nome da turma: ")

    if nome_turma in materias:

        del materias[nome_turma]

        print("Turma removida!")

    else:
        print("Turma não encontrada.")

def parecer_aluno():

    nome = input("Nome do aluno: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            if len(aluno["notas"]) == 0:
                print("Aluno sem notas.")
                return

            media = sum(aluno["notas"].values()) / len(aluno["notas"])

            print(f"Média: {media:.1f}")

            if media >= 7:
                return f"{Fore.GREEN}Aprovado{Fore.RESET}"
            
            elif media >= 5:
                return f"{Fore.YELLOW}Em Recuperação{Fore.RESET}"
            
            else:
                return f"{Fore.RED}Em Recuperação{Fore.RESET}"
            

    print("Aluno não encontrado.")

#menus #COMPLETOS
def menu_aluno():
    while True:
        print("\n --- MENU DE AÇÕES DO ALUNO\\RESPONSÁVEL ---")
        print("1 - Visualizar parecer do aluno")
        print("0 - Sair do Sistema")
        actAluno = input("\nO que você deseja fazer: ")

        if actAluno == "1":
            parecer_aluno()
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
            cadastrar_aluno()
        elif actSecre == "2":
            remover_aluno()
        elif actSecre == "3":
            cadastrar_prof()
        elif actSecre == "4":
            remover_prof()
        elif actSecre == "5":
            cadastrar_turma()
        elif actSecre == "6":
            remover_turma()
        elif actSecre == "7":
            editar_alunos()
        elif actSecre == "8":
            editar_prof()
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