from model.livro_model import *
from view.view_livro import *

class LivroController:
    def __init__(self):
        self.model = LivroModel()


    def cadastrar_livro(self):
        try:
            titulo, ano_publicacao, id_autor = cadastrar_dados_livro()
            if not titulo or not ano_publicacao or not id_autor:
                mensagem("Todos os campos são obrigatórios.")
                return
            self.model.cadastrar_livro(titulo, ano_publicacao, id_autor)
            mensagem("Livro cadastrado com sucesso!")   
        except Exception as e:
            mensagem(f"Erro ao cadastrar livro: {e}")

    def listar_livros(self):
        try:
            livros = self.model.listar_livros()
            listar_livros(livros)
        except Exception as e:
            mensagem(f"Erro ao listar livros: {e}")

    def atualizar_livro(self):
        try:
            idlivro = id_livro()
            if idlivro is None:
                return
            titulo, ano_publicacao, id_autor = cadastrar_dados_livro()
            self.model.atualizar_livro(idlivro, titulo, ano_publicacao, id_autor)
            mensagem("Livro atualizado com sucesso!")
        except Exception as e:
            mensagem(f"Erro ao atualizar livro: {e}")


    def excluir_livro(self):
        try:
            idlivro = id_livro()
            if idlivro is None:
                return
            self.model.excluir_livro(idlivro)
            mensagem("Livro excluído com sucesso!")
        except Exception as e:
            mensagem(f"Erro ao excluir livro: {e}")