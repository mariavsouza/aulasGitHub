from datetime import datetime
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
 
        return True,
 
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
    while True:
        nome = input("Nome do aluno: ")
        if not validar_nome(nome):
            return False
        
        data_nascimento = input("Data de Nascimento: ")
        if not validar_nascimento(data_nascimento):
            return False

        turma = input("Turma: ")
        if not validar_turma(turma):
            return False

        dados = [nome, data_nascimento, turma]
        alunos.append(dados)


        print("Aluno cadastrado com sucesso!")
        break


def listar_aluno():
    ...

def remover_aluno():
    ...

def editar_dados():
    ...

def adicionar_notas():
    id_aluno = int(input("Digite o ID do aluno: "))

    if id_aluno not in alunos:
        print("Aluno não encontrado.")
        return

    entrada = float(input("Digite a nota: "))
    alunos[id_aluno]["notas"].append(entrada)

    print("Nota adicionada!")

def remover_notas():
    id_aluno = int(input("Digite o ID do aluno: "))

    if id_aluno not in alunos:
        print("Aluno não encontrado :( ")
        return

    if not alunos[id_aluno]["notas"]:
        print("Esse aluno não possui notas :(")
        return

    print("Notas:", alunos[id_aluno]["notas"])
    nota = float(input("Digite a nota que deseja remover: "))

    if nota in alunos[id_aluno]["notas"]:
        alunos[id_aluno]["notas"].remove(nota)
        print("Nota removida!")
    else:
        print("Nota não encontrada.")

def caucular_media():
    id_aluno = int(input("Digite o ID do aluno: "))

    if id_aluno not in alunos:
        print("Aluno não encontrado :(")
        return

    notas = alunos[id_aluno]["notas"]

    if len(notas) > 0:
        media = sum(notas) / len(notas)
        print(f"\nVocê digitou {len(notas)} notas.")
        print(f"A média final é: {media:.2f}")
    else:
        print("Nenhuma nota foi registrada :(")

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