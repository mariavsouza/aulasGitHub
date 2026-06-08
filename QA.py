from datetime import datetime
from funcoes import *

notas = []
alunos = []

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
 
 
def calcular_media(notas_aluno):
    if not alunos:
        print("Nenhum aluno cadastrado no sistema.")
        return

    print("\n--- Lista de Alunos ---")
    for i, aluno in enumerate(alunos, start=1):
        print(f"Aluno {i}: Nome: {aluno[0]}; Data de nascimento: {aluno[1]}; Turma: {aluno[2]}")
    
    id_aluno = int(input("Digite o ID do aluno que você quer calcular a média: "))

    if id_aluno < 1 or id_aluno > len(alunos):
        print("Aluno não encontrado :(")
        return 

    indice_real = id_aluno - 1
    notas_aluno = alunos[indice_real][3]

    if len(notas_aluno) > 0:
        media = sum(notas_aluno) / len(notas_aluno)
        print(f"\nO aluno possui {len(notas_aluno)} notas registradas.")
        print(f"A média final é: {media:.2f}")
    else:
        print("Nenhuma nota foi registrada para este aluno ainda.")
 
def validar_media():
    ...
 
 
def definir_situacao():
    if not alunos:
        print("Nenhum aluno cadastrado no sistema.")
        return
    
    print("--- ALUNOS CADASTRADOS ---")
    for i, aluno in enumerate(alunos, start=1):
        print(f"Aluno {i}: Nome: {aluno[0]}; Data de nascimento: {aluno[1]}; Turma: {aluno[2]}")
    id_aluno = int(input("Digite o ID do aluno que você quer ver a situação: "))

    if id_aluno < 1 or id_aluno > len(alunos):
        print("Aluno não encontrado.")

    if id_aluno not in notas:
        print(f"Nenhuma nota cadastrada para o ID: {id_aluno}")
        return

    media = sum(notas[id_aluno]) / len(notas[id_aluno])
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    VERMELHO = "\033[31m"
    RESET = "\033[m"

    if media >= 7.0:
        situacao = f"{VERDE}Aprovado{RESET}"
    elif 5.0 <= media < 7.0:
        situacao = f"{AMARELO}Em recuperação{RESET}"
    else:
        situacao = f"{VERMELHO}Reprovado{RESET}"

    print(f"Aluno ID: {id_aluno} | Média: {media:.2f} | Situação: {situacao}")


def cadastrar_aluno():
    while True:
        nome = input("Nome do aluno: ")
        if not validar_nome(nome):
            return 
        
        data_nascimento = input("Data de Nascimento: ")
        if not validar_nascimento(data_nascimento):
            return 

        turma = input("Turma: ")
        if not validar_turma(turma):
            return 
        
        notas = []

        dados = [nome, data_nascimento, turma, notas]
        alunos.append(dados)
        
        print("Aluno cadastrado com sucesso!")
        break


def listar_aluno():
    if not alunos:
        print("Nenhum aluno foi cadastrado ainda")
        return 

    else:
        print("\n--- LISTA DE ALUNOS ---")
        for i, aluno in enumerate(alunos, start=1):
            print(f"Aluno {i}: Nome: {aluno[0]}; Data de nascimento: {aluno[1]}; Turma: {aluno[2]}.")

def remover_aluno(id_aluno):
    for aluno in alunos:
        if aluno["id"] == id_aluno:
            alunos.remove(aluno)
            print(f"Aluno {id_aluno} removido com sucesso.")
            return
    print(f"Aluno {id_aluno} não encontrado.")

def remover_professor(id_professor):
    for professor in professor:
        if professor["id"] == id_professor:
            professor.remove(professor)
            print(f"Professor {id_professor} removido com sucesso.")
            return
    print(f"Professor {id_professor} não encontrado.")

def remover_turma(id_turma):
    for turma in turma:
        if turma["id"] == id_turma:
            turma.remove(turma)
            print(f"Turma {id_turma} removida com sucesso.")
            return
    print(f"Turma {id_turma} não encontrada.")

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
            definir_situacao()
        elif opcao == "9":
            buscar_aluno()
        elif opcao == "0":
            print("\nVocê saiu do Sistema Instituto D'Souza. Encerando sistema...")
            break
        else:
            print("Opção inválida! Escolha uma das opções mostradas a baixo.")

print("\n----- Bem vindo ao sistema do Instituto D'Souza -----")
menu()