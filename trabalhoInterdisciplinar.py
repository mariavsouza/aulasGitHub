from datetime import datetime
from colorama import init, Fore
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
            return 
 

    except ValueError:
        print("Formato inválido. Use DD/MM/AAAA.")
        return 
 
 
def validar_turma(turma):
    if not turma.strip():
        print("A turma não pode estar vazia.")

        return 
 
def validar_notas(notas):
    if not isinstance(notas, list):
        print("As notas devem ser uma lista.")
        return 
 
    for nota in notas:
        if not isinstance(nota, (int, float)):
            print("Todas as notas devem ser numéricas.")
            return
 
        if nota < 0 or nota > 10:
            print("As notas devem estar entre 0 e 10.")
            return
 
def calcular_media(notas):
    ...
 
def definir_situacao():
    media = input("Digite sua média: ")
    if media >= 7:
        return f"{Fore.GREEN}Aprovado{Fore.RESET}"
    elif media >= 5:
        return f"{Fore.YELLOW}Em Recuperação{Fore.RESET}"
    else:
        return f"{Fore.RED}Em Recuperação{Fore.RESET}"

def cadastrar_aluno(): #completo
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

def listar_aluno():#completo
    if not alunos:
        print("Nenhum aluno foi cadastrado ainda")
        return 

    else:
        print("\n--- LISTA DE ALUNOS ---")
        for i, aluno in enumerate(alunos, start=1):
            print(f"Aluno {i}: Nome: {aluno[0]}; Data de nascimento: {aluno[1]}; Turma: {aluno[2]}.")

    print("\n--- LISTA DE ALUNOS ---")
    
    for i, aluno in enumerate(alunos, start=1):
        print(f"Aluno {i}: Nome: {aluno[0]}; Idade: {aluno[1]} anos; Cidade: {aluno[2]}.")
 

def remover_aluno(id_aluno, nota): #refazer
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

def adicionar_notas():#completo
    if not alunos:
        print("Nenhum aluno cadastrado no sistema.")
        return

    print("\n--- Lista de Alunos ---")
    for i, aluno in enumerate(alunos, start=1):
        print(f"Aluno {i}: Nome: {aluno[0]}; Data de nascimento: {aluno[1]}; Turma: {aluno[2]}")
    id_aluno = int(input("Digite o ID do aluno que você quer adicionar uma nota: "))

    if id_aluno < 1 or id_aluno > len(alunos):
        print("Aluno não encontrado.")

    entrada = float(input("Digite a nota: "))
    indice_real = id_aluno - 1
    alunos[indice_real][3].append(entrada)

def remover_notas(id_aluno, nota):#testar
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

def caucular_media():#testar
    notas.append()
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
