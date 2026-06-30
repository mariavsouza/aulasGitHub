# Aqui vamos colocar apenas o trabalho oficial, tudo que tinha nele eu transportei para o arquivo esboço. e as def's e validações 
# treinamos em seus respectivos arquivos e depois juntamos tudo aqui para fiucar melhor a organizaçãoimport mysql.connector

import mysql.connector
from mysql.connector import Error

CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "sua_senha",
    "database": "sistema_escolar",
}


def conectar():
    try:
        conexao = mysql.connector.connect(**CONFIG)
        if conexao.is_connected():
            print(f"Conectado ao banco '{CONFIG['database']}' com sucesso!")
            print(f"Versão do servidor MySQL: {conexao.get_server_info()}")
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None


def listar_tabelas(conexao):
    cursor = conexao.cursor()
    cursor.execute("SHOW TABLES;")
    tabelas = cursor.fetchall()
    print("Tabelas encontradas:")
    for (tabela,) in tabelas:
        print(f"  - {tabela}")
    cursor.close()


if __name__ == "__main__":
    conexao = conectar()

    if conexao:
        listar_tabelas(conexao)
        conexao.close()
        print("Conexão encerrada.")