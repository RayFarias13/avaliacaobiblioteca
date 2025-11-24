from controller.livro_controller import LivroController
from controller.autor_controller import AutorController
from view.view_autor import menu_autor
from view.view_livro import menu_livro


def main():
    print("\n=== Sistema de Gerenciamento de Biblioteca ===")
    while True:
        try:
            print("\n===== MENU PRINCIPAL =====")
            print("1 - Gerenciar Autores")
            print("2 - Gerenciar Livros")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
               submenu_autor()
            elif opcao == "2":
                submenu_livro()   
            elif opcao == "0":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente1.")
        except Exception as e:
            print(f"Erro no menu principal: {e}")





def submenu_livro():
    res_livro = LivroController()   
    while True:
        opcaolivro = menu_livro()
        if opcaolivro == "1":
            res_livro.cadastrar_livro()
        elif opcaolivro == "2":
            res_livro.listar_livros()
        elif opcaolivro == "3":
            res_livro.atualizar_livro()
        elif opcaolivro == "4":
            res_livro.excluir_livro()
        elif opcaolivro == "5":
            return
        elif opcaolivro == "0":
            print("Saindo do programa...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")

def submenu_autor():
    res_autor = AutorController()   
    while True:
        opcaoautor = menu_autor()
        if opcaoautor == "1":
            res_autor.cadastrar_autor()
        elif opcaoautor == "2":
            res_autor.listar_autores()
        elif opcaoautor == "3":
            res_autor.atualizar_autor()
        elif opcaoautor == "4":
            res_autor.excluir_autor()
        elif opcaoautor == "5":
            return
        elif opcaoautor == "0":
            print("Saindo do programa...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")



if __name__ == "__main__":
    main()







