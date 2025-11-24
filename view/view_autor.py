def menu_autor():
    print("\n--- Menu Autor ---")
    print("1 - Cadastrar Autor")
    print("2 - Listar Autores")
    print("3 - Atualizar Autor")
    print("4 - Excluir Autor")
    print("5 - Voltar ao Menu Principal")
    print("0 - Sair")

    return input("Escolha uma opção: ")

def cadastrar_dados_autor():
    nome = input("\nNome do Autor: ")
    nacionalidade = input("Nacionalidade: ")
    return nome, nacionalidade

def id_autor():
    try:
        return int(input("\nInforme o ID do autor: "))
    except ValueError:
        print("ID inválido. Por favor, insira um número inteiro.")
        return None

def listar_autores(autores):
    print("\n---- Lista de Autores ----")
    if not autores:
        print("Nenhum autor cadastrado.")
    else:
        for autor in autores:
            
            print(f"ID: {autor[0]}, Nome: {autor[1]}, Nacionalidade: {autor[2]}")
    print("--------------------------")

def mensagem(texto):
    print(f"\n{texto}")