import mysql.connector
from mysql.connector import Error

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

def validar_dados():
    ...

def cadastrar_aluno():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))
    turma = input("Turma: ")
    notas = input("Notas: ")
    media = ("Media: ")
    Situação = ("Situação do aluno: ")

    sql = """
    INSERT INTO alunos (nome, idade, turma)
    VALUES (%s, %s, %s)
    """

    valores = (nome, idade, turma)

    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

    print("Aluno cadastrado com sucesso!")


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
            print("você saiu do Sistema Instituto D'Souza")
            break
        else:
            print("Opção inválida!")

print("Bem vindo ao sistema do Instituto D'Souza")
menu()
