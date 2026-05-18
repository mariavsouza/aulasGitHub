import mysql.connector
from mysql.connector import Error
from datetime import datetime
notas = []
alunos = []

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
    
def criar_database():
    conexao = criar_conexao()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS sistemaEscolar;")
        cursor.execute("USE DATABASE sistemaEscolar;")
        print("Banco de dados criado com sucesso! :) ")

    conexao.commit()
    cursor.close()
    conexao.close()

def criar_table():
    conexao = criar_conexao()
 
    if conexao:
        cursor = conexao.cursor()
    
        criar_table = """
        CREATE TABLE IF NOT EXISTS alunos(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        data_nascimento DATE,
        turma VARCHAR(50),
        notas VARCHAR(255),
        media DECIMAL(4, 2),
        situacao VARCHAR(50)
        );"""

    cursor.execute(criar_table)
    conexao.commit()
    cursor.close()
    conexao.close()

def validar_nome(nome):
    if not nome.strip():
        return False, "O nome não pode estar vazio."
 
    if not all(parte.isalpha() for parte in nome.replace(" ", "").split()):
        return False, "O nome deve conter apenas letras."
 
    return True, "Nome válido."
 
 
def validar_nascimento(data_nascimento):
    try:
        data = datetime.strptime(data_nascimento, "%d/%m/%Y")
 
        if data > datetime.now():
            return False, "A data de nascimento não pode ser futura."
 
        return True, "Data de nascimento válida."
 
    except ValueError:
        return False, "Formato inválido. Use DD/MM/AAAA."
 
 
def validar_turma(turma):
    if not turma.strip():
        return False, "A turma não pode estar vazia."
 
    return True, "Turma válida."
 
def validar_notas(notas):
    if not isinstance(notas, list):
        return False, "As notas devem ser uma lista."
 
    for nota in notas:
        if not isinstance(nota, (int, float)):
            return False, "Todas as notas devem ser numéricas."
 
        if nota < 0 or nota > 10:
            return False, "As notas devem estar entre 0 e 10."
 
    return True, "Notas válidas."
 
 
def calcular_media(notas):
    return sum(notas) / len(notas)
 
 
def validar_media(media):
    if not isinstance(media, (int, float)):
        return False, "A média deve ser numérica."
 
    if media < 0 or media > 10:
        return False, "A média deve estar entre 0 e 10."
 
    return True, "Média válida."
 
 
def definir_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def cadastrar_aluno():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    nome = input("Nome do aluno: ")
    if not validar_nome():
        return False
    
    data_nascimento = datetime(input("Data de Nascimento: "))
    if not validar_nascimento():
        return False

    turma = input("Turma: ")
    if not validar_turma():
        return False

    dados = [nome, data_nascimento, turma]
    alunos.append(dados)

    print("Aluno cadastrado com sucesso!")

    sql = """
    INSERT INTO alunos (nome, data_nascimento, turma)
    VALUES (%s, %s, %s)
    """

    valores = (nome, data_nascimento, turma)

    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

    print("Aluno cadastrado com sucesso!")

def listar_aluno():
    id_aluno = int(input("Digite o ID do aluno: "))

    if id_aluno not in alunos:
        print("Aluno não encontrado.")
        return


    print("\n--- LISTA DE ALUNOS ---")
    
    for i, aluno in enumerate(alunos, start=1):
        print(f"Aluno {i}: Nome: {aluno[0]}; Idade: {aluno[1]} anos; Cidade: {aluno[2]}.")
 

def remover_aluno(id_aluno, nota):
    for i, aluno in enumerate(alunos):
        if aluno["id"] == id.aluno:
            if nota in aluno["notas"]:
                aluno["notas"].remove.nota
                print(f"\nNota (nota) removida! Notas de {aluno['nome']}: {aluno['notas']}")
                return True
            print(f"\nNota (nota) não encontrada para {aluno['nome']}.")
            return False
    print(f"\nAluno com ID (id_aluno) não encontrado.")
    return False

def editar_dados(id_aluno, novo_nome):
    for aluno in alunos:
        if aluno["id"] == id_aluno:
            aluno["nome"] = novo_nome
            print(f"\nDados atualizados: {aluno['id']} - {aluno['nome']}")
            return True
    print(f"\nAluno com ID {id_aluno} não encontrado.")
    return False

def adicionar_notas(id_aluno, nota):
    for aluno in alunos:
        if aluno["id"] == id_aluno:
            aluno["notas"].append(nota)
            print(f"\nNota {nota} adicionada! Notas de {aluno['nome']}: {aluno['notas']}")
            return True
    print(f"\nAluno com ID {id_aluno} não encontrado.")
    return False

def remover_notas(id_aluno, nota):
    for aluno in alunos:
        if aluno["id"] == id_aluno:
            if nota in aluno["notas"]:
                aluno["notas"].remove(nota)
                print(f"\nNota {nota} removida! Notas de {aluno['nome']}: {aluno['notas']}")
                return True
            print(f"\nNota {nota} não encontrada para {aluno['nome']}.")
            return False
    print(f"\nAluno com ID {id_aluno} não encontrado.")
    return False

def caucular_media():
    notas.append()
    notas = []
    while True:
        entrada = float(input("Digite uma nota (ou -1 para calcular a média): "))
        
        if entrada == -1:
            break  
            
        else:
            notas.append(entrada)


    if len(notas) > 0:
        media = sum(notas) / len(notas)
        print(f"\nVocê digitou {len(notas)} notas.")
        print(f"A média final é: {media:.2f}")
    else:
        print("Nenhuma nota foi registrada.")

def situção_aluno():
    ...

def buscar_aluno():
    ...

def menu():
    while True:
        print("\n --- MENU ---")
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
 
        opcao = input("\nEscolha uma opção: ")
 
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
            print("\nVocê saiu do Sistema Instituto D'Souza. Encerando sistema...")
            break
        else:
            print("Opção inválida! Escolha uma das opções mostradas a baixo.")

print("\n----- Bem vindo ao sistema do Instituto D'Souza -----")
menu()
