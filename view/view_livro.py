def menu_livro():
    print("\n--- Menu Livro ---")
    print("1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Atualizar Livro")
    print("4 - Excluir Livro")
    print("5 - Voltar ao Menu Principal")
    print("6 - Sair")

    return  input("Escolha uma opção: ")

def cadastrar_dados_livro():
    titulo = input("\nTítulo do Livro: ")
    ano_publicacao = input("Ano de Publicação: ")
    autor_id = input("ID do Autor: ")
    return titulo, ano_publicacao, autor_id 

def id_livro():
    try:
        return int(input("\nInforme o ID do livro: "))
    except ValueError:
        print("ID inválido. Por favor, insira um número inteiro.")
        return None

def listar_livros(livros):
    print("\n---- Lista de Livros ----")
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    for livro in livros:
        print(f"ID: {livro[0]}, Título: {livro[1]}, Ano de Publicação: {livro[2]}, Autor: {livro[5]}")
    print("--------------------------")


def mensagem (texto):
    print(texto)