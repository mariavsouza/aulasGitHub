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
        cursor.execute("CREATE DATABASE IF NOT EXISTS sistemaEscolar")
        print("Banco de dados criado com sucesso! :) ")

    cursor.close()
    conexao.close()

def criar_table():
    conexao = criar_conexao()
 
    if conexao:
        cursor = conexao.cursor()
        criar_table = """
        CREATE TABLE IF NOT EXISTS alunos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        data_nascimento DATETIME,
        turma VARCHAR(50),
        notas VARCHAR(255),
        media DECIMAL(4, 2),
        situacao VARCHAR(50)"""

    cursor.execute(criar_table)
    cursor.close()
    conexao.close()

print("Bem vindo ao sistema da escola Sepa prime")
 
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
            Cadastrar_aluno()
        elif opcao == "2":
            Listar_aluno()
        elif opcao == "3":
            Remover aluno()
        elif opcao == "4":
            Editar_dados_do_aluno()
        elif opcao == "5":
            Adicionar_notas()
        elif opcao == "6":
            Remover_notas()
        elif opcao == "7":
            Caucular_media_do_aluno()
        elif opcao == "8":
            "Situção_do_aluno"()
        elif opcao == "9":
            Buscar_por_aluno()
        elif opcao == "0":
            print("você saiu do Sistema da escola sepa prime")
            break
        else:
            print("Opção inválida!")
 
menu()