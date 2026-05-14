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




    # addfsadfas
    # dfsad
    # fsad
    # finallysadf
    # sad
    # finallydf
    # staticmethodsad
    