def menu_autor():
    print("\n--- Menu Autor ---")
    print("1 - Cadastrar Autor")
    print("2 - Listar Autores")
    print("3 - Atualizar Autor")
    print("4 - Excluir Autor")
    print("5 - Voltar ao Menu Principal")
    
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
            # Aqui estou assumindo que 'autor' é um Objeto (vido do seu model.py).
            # Se sua dupla estiver usando listas/tuplas diretas do banco, 
            # altere para autor[0], autor[1], etc.
            print(f"ID: {autor.id}, Nome: {autor.nome}, Nacionalidade: {autor.nacionalidade}")
    print("--------------------------")

def mensagem(texto):
    print(f"\n{texto}")