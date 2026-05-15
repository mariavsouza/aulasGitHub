from datetime import datetime
notas = []
def validar_nome(nome):
    if not nome.strip():
        print("O nome não pode estar vazio.")
        return False
 
    if not all(parte.isalpha() for parte in nome.replace(" ", "").split()):
        print("O nome deve conter apenas letras.")
        return False
 
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

    cadastro = []

    nome = input("Nome do aluno: ")
    if not validar_nome():
        return False
    data_nascimento = datetime(input("Data de Nascimento: "))
    validar_nascimento()
    turma = input("Turma: ")
    validar_turma()

    dados = [nome, data_nascimento, turma]
    cadastro.append(dados)

    print("Aluno cadastrado com sucesso!")


def listar_aluno():
    ...

def remover_aluno():
    ...

def editar_dados():
    ...

def adicionar_notas():
    entrada = float(input("Digite a nota: "))
    notas.append(entrada)
    print("Nota adicionada!")

def remover_notas():
    ...

def caucular_media():
    
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