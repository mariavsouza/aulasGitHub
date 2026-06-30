#importações de recursos externos
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from colorama import Fore, init
init()

#id's
id_aluno = 1
id_professor = 1

#listas pré estabelecidas 
alunos = []
professores = []
notas = []
materias = {
    "1EM": ["A", "B", "R"],
    "2EM": ["A", "B", "R"],
    "3EM": ["A", "B", "R"]
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

    if not all(parte.isalpha() for parte in nome.split()):
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


def validar_materia(turma, materia):

    if turma not in materias:
        print("Turma não encontrada.")
        return False

    if materia not in materias[turma]:
        print("Matéria inválida.")
        return False

    return True


#cadastros
def cadastrar_aluno():
    global id_aluno

    nome = input("Nome do aluno: ").strip()

    if not validar_nome(nome):
        return

    data_nascimento = input("Data de Nascimento: ").strip()

    if not validar_nascimento(data_nascimento):
        return

    turma = input("Turma (1EM, 2EM ou 3EM): ").upper().strip()

    if turma not in materias:
        print("Turma inválida.")
        return

    aluno = {
        "id": id_aluno,
        "nome": nome,
        "nascimento": data_nascimento,
        "turma": turma,
        "notas": {}
    }

    alunos.append(aluno)
    id_aluno += 1

    conn = criar_conexao() 
    cursor = conn.cursor() 
    cursor.execute("SELECT id FROM turmas WHERE nome=%s", (turma,)) 
    res = cursor.fetchone() 

    if not res:
        cursor.execute("INSERT INTO turmas (nome) VALUES (%s)", (turma,)) 
        conn.commit() 
        turma_id = cursor.lastrowid 
    else: turma_id = res[0] 
    
    sql = "INSERT INTO alunos (nome, data_nascimento, turma_id) VALUES (%s, %s, %s)" 
    cursor.execute(sql, (nome, converter_data(nascimento), turma_id)) 
    conn.commit()  

    print(f"Aluno cadastrado com sucesso! ID: {aluno['id']}")

    cursor.close() 
    conn.close()

def cadastrar_prof():
    global id_professor

    nome = input("Nome do Professor: ").strip()

    if not validar_nome(nome):
        return

    turma = input("Turma (1EM, 2EM ou 3EM): ").upper().strip()

    if turma not in materias:
        print("Turma inválida.")
        return

    print("\nMatérias disponíveis:")
    print("\nA | Algorítimos;\nB | Banco de Dados\nR | Requisitos")

    materia = input("\nQue matéria você leciona?: ").upper().strip()

    if materia not in materias[turma]:
        print("Matéria inválida.")
        return

    professor = {
        "id": id_professor,
        "nome": nome,
        "turma": turma,
        "materia": materia
    }

    professores.append(professor)
    id_professor += 1

    conn = criar_conexao() 
    cursor = conn.cursor() 

    cursor.execute("SELECT id FROM turmas WHERE nome=%s", (turma,)) 
    turma_id = cursor.fetchone()[0] 

    sql = "INSERT INTO professores (nome, turma_id, materia) VALUES (%s, %s, %s)" 
    cursor.execute(sql, (nome, turma_id, materia)) 
    conn.commit()

    print(f"Professor cadastrado com sucesso! ID: {professor['id']}")

    cursor.close() 
    conn.close()

def cadastrar_turma():

    nome_turma = input("Digite o nome da turma: ")

    if nome_turma in materias:
        print("Turma já cadastrada.")
        return

    materias[nome_turma] = ["A", "B", "R"]

    print("Turma cadastrada com sucesso!")


#notas
def adicionar_nota():
    conn = criar_conexao()
    cursor = conn.cursor()

    nome = input("Nome do aluno: ")

    for aluno in alunos:
        cursor.execute("SELECT id FROM alunos WHERE nome=%s", (nome,)) 
        aluno = cursor.fetchone()

        if aluno["nome"].lower() == nome.lower():

            materia = input("Matéria: ").upper()

            cursor.execute("SELECT id FROM materias WHERE codigo=%s", (materia,))
            mat = cursor.fetchone()

            if not validar_materia(aluno["turma"], materia):
                return

            try:
                nota = float(input("Nota: "))
            except ValueError:
                print("Nota inválida.")
                return

            if nota < 0 or nota > 10:
                print("Nota inválida.")
                return

            if materia not in aluno["notas"]:
                aluno["notas"][materia] = []

            aluno["notas"][materia].append(nota)

            sql = "INSERT INTO notas (aluno_id, materia_id, nota) VALUES (%s, %s, %s)" 
            cursor.execute(sql, (aluno[0], mat[0], nota)) 
            conn.commit()

            print("Nota adicionada com sucesso!")
            cursor.close() 
            conn.close()
            return


    print("Aluno não encontrado.")


def editar_nota():

    nome = input("Nome do aluno: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            materia = input("Matéria: ").upper()

            if materia in aluno["notas"]:

                print("Notas:", aluno["notas"][materia])

                try:
                    indice = int(input("Qual nota deseja editar?: ")) - 1
                    nova_nota = float(input("Nova nota: "))
                except:
                    print("Entrada inválida.")
                    return

                if indice < 0 or indice >= len(aluno["notas"][materia]):
                    print("Índice inválido.")
                    return

                aluno["notas"][materia][indice] = nova_nota

                print("Nota atualizada!")

            else:
                print("Matéria não encontrada.")

            return

    print("Aluno não encontrado.")


def remover_nota():

    nome = input("Nome do aluno: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            materia = input("Matéria: ").upper()

            if materia in aluno["notas"]:

                print("Notas:", aluno["notas"][materia])

                try:
                    indice = int(input("Qual nota deseja remover?: ")) - 1
                except:
                    print("Entrada inválida.")
                    return

                if indice < 0 or indice >= len(aluno["notas"][materia]):
                    print("Índice inválido.")
                    return

                aluno["notas"][materia].pop(indice)

                print("Nota removida!")

            else:
                print("Matéria não encontrada.")

            return

    print("Aluno não encontrado.")


#remover
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

#outros
def editar_aluno():
    nome = input("Nome do aluno que deseja editar: ").strip()

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():

            print("\nO que deseja editar?")
            print("1 - Nome")
            print("2 - Data de Nascimento")
            print("3 - Turma")

            opcao = input("Escolha: ").strip

            if opcao == "1":
                novo_nome = input("Novo nome: ").strip()
                if validar_nome(novo_nome):
                    aluno["nome"] = novo_nome
                    print("Nome atualizado com sucesso!")
            elif opcao == "2":
                nova_data = input("Nova data de nascimento: ").strip()
                if validar_nascimento(nova_data):
                    aluno["nascimento"] = nova_data
                    print("Data de nascimento atualizada!")
            elif opcao == "3":
                nova_turma = input("Nova turma: ").upper().strip()
                if nova_turma in materias:
                    aluno["turma"] = nova_turma
                    print("Turma atualizada!")
                else:
                    print("Turma inválida.")
            else:
                print("Opção inválida.")
            return
        
    print("Aluno não encontrado.")

def editar_prof():
    nome = input("Nome do professor que deseja editar: ").strip()

    for professor in professores:
        if professor["nome"].lower() == nome.lower():

            print("\nO que deseja editar?")
            print("1 - Nome")
            print("2 - Turma")
            print("3 - Matéria")

            opcao = input("Escolha: ")

            if opcao == "1":
                novo_nome = input("Novo nome: ").strip()
                if validar_nome(novo_nome):
                    professor["nome"] = novo_nome
                    print("Nome atualizado com sucesso!")
            elif opcao == "2":
                nova_turma = input("Nova turma: ").upper().strip()
                if nova_turma in materias:
                    professor["turma"] = nova_turma
                    print("Turma atualizada!")
                else:
                    print("Turma inválida.")
            elif opcao == "3":
                print("\nMatérias disponíveis:")
                print("A | Algorítimos")
                print("B | Banco de Dados")
                print("R | Requisitos")

                nova_materia = input("Nova matéria: ").upper().strip()

                if validar_materia(professor["turma"], nova_materia):
                    professor["materia"] = nova_materia
                    print("Matéria atualizada!")
            else:
                print("Opção inválida.")

            return

    print("Professor não encontrado.")

#parecer do aluno
def parecer_aluno():

    nome = input("Nome do aluno: ").strip()

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():

            print(f"\nID: {aluno['id']}")
            print(f"Nome do Aluno: {aluno['nome']}")
            print(f"Data de Nascimento: {aluno['nascimento']}")
            print(f"Turma do Aluno: {aluno['turma']}")

            if not aluno["notas"]:
                print("Sem notas cadastradas.")
                return

            for materia, notas in aluno["notas"].items():

                print(f"\nMatéria: {materia}")

                for i, nota in enumerate(notas, start=1):
                    print(f"Nota {i}: {nota}")

                media = sum(notas) / len(notas)
                print(f"Média: {media:.1f}")

                if media >= 7:
                    situacao = f"{Fore.GREEN}Aprovado{Fore.RESET}"
                elif media >= 5:
                    situacao = f"{Fore.YELLOW}Em Recuperação{Fore.RESET}"
                else:
                    situacao = f"{Fore.RED}Reprovado{Fore.RESET}"

                print(f"Situação: {situacao}")

            return

    print("Aluno não encontrado.")

#menus | COMPLETOS
def menu_aluno():
    while True:
        print("\n --- MENU DE AÇÕES DO ALUNO\\RESPONSÁVEL ---")
        print("1 - Visualizar parecer do aluno")
        print("2 - Trocar Forma de Login")
        print("0 - Sair do Sistema")

        actAluno = input("\nO que você deseja fazer: ").strip()

        if actAluno == "1":
            parecer_aluno()
        elif actAluno == "2":
            menu_inicial()
        elif actAluno == "0":
           print("\nVocê saiu do Sistema Instituto D'Souza. Encerando serviços...")
           break
        else:
            print(">>ERRO<<\nEscolha uma opção válida mostrada acima!")
            continue

def menu_professor():
    
    nome = input("Digite seu nome: ").strip()
    while True:

        professor_encontrado = None

        for prof in professores:
            if prof["nome"].lower() == nome.lower():
                professor_encontrado = prof
                break

        if not professor_encontrado:
            print("Usuário não encontrado!")
            return

        print("\n --- MENU DE AÇÕES DO PROFESSOR ---")
        print("1 - Adicionar Notas")
        print("2 - Remover Notas")
        print("3 - Editar Notas")
        print("4 - Trocar Forma de Login")
        print("0 - Sair do Sistema ")

        actProf = input("\nO que você deseja fazer: ")

        if actProf == "1":
            adicionar_nota()
        elif actProf == "2":
            remover_nota()
        elif actProf == "3":
            editar_nota()
        elif actProf == "4":
            menu_inicial()
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
        print("5 - Cadastrar Turma")
        print("6 - Remover Turma")
        print("7 - Editar Dados dos Aluno")
        print("8 - Editar Dados do Professor")
        print("9 - Trocar Forma de Login")
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
            editar_aluno()
        elif actSecre == "8":
            editar_prof()
        elif actSecre == "9":
            menu_inicial()
        elif actSecre == "0":
           print("\nVocê saiu do Sistema Instituto D'Souza. Encerando serviços...")
           break
        else:
            print(">>ERRO<<\nEscolha uma opção válida mostrada acima!")
            continue


def menu_inicial():
    while True:
        print("\n --- OPÇÕES DE LOGIN ---")
        print("1 - Aluno\\Responsável")
        print("2 - Professor(a)")
        print("3 - Secretário")
        print("0 - Sair do Sistema")

        login = input("\nQual a sua forma de login?: ")

        if login == "1":
            menu_aluno()
        elif login == "2":
            menu_professor()
        elif login == "3":
            menu_secretario()
        elif login == "0":
           print("\nVocê saiu do Sistema Instituto D'Souza. Encerando serviços...")
           break
        else:
            print(">>ERRO<<\nEscolha uma opção válida mostrada acima!")
            continue

print("\n----- Bem vindo ao sistema do Instituto D'Souza -----")
menu_inicial()