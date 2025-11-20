from controller.livro_controller import livro_controller
from view.livro_view import menu_livro


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
    controller = livro_controller.LivroController()
    while True:
        opcao = menu_livro()
        if opcao == "1":
            controller.cadastrar_livro()
        elif opcao == "2":
            controller.listar_livros()
        elif opcao == "3":
            controller.atualizar_livro()
        elif opcao == "4":
            controller.excluir_livro()
        elif opcao == "5":
            return
        elif opcao == "6":
            print("Saindo do programa...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")



if __name__ == "__main__":
    main()







