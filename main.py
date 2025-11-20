from controller.livro_controller import LivroController
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
                pass
                #submenu_autor()
                #Artur


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
        elif opcaolivro == "6":
            print("Saindo do programa...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")



if __name__ == "__main__":
    main()







