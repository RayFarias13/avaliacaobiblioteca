from model.autor_model import *
from view.view_autor import *

class AutorController:
    def __init__(self):
        self.model = AutorModel()

    def cadastrar_autor(self):
        try:
            nome, nacionalidade = cadastrar_dados_autor()
            if not nome or not nacionalidade:
                mensagem("Todos os campos são obrigatórios.")
                return
            
            self.model.cadastrar_autor(nome, nacionalidade)
            mensagem("Autor cadastrado com sucesso!")
        except Exception as e:
            mensagem(f"Erro ao cadastrar autor: {e}")

    def listar_autores(self):
        try:
            autores = self.model.listar_autores()
            listar_autores(autores)
        except Exception as e:
            mensagem(f"Erro ao listar autores: {e}")

    def atualizar_autor(self):
        try:
            if listar_autores(self.model.listar_autores()) is []:
                pass
            else:
                listar_autores(self.model.listar_autores())
                idautor = id_autor()
                if idautor is None:
                    return

                nome, nacionalidade = cadastrar_dados_autor()
                
                self.model.atualizar_autor(idautor, nome, nacionalidade)
                mensagem("Autor atualizado com sucesso!")
        except Exception as e:
            mensagem(f"Erro ao atualizar autor: {e}")

    def excluir_autor(self):
        try:
            if listar_autores(self.model.listar_autores()) is []:
                pass
            else:
                listar_autores(self.model.listar_autores())
            
                idautor = id_autor()
                if idautor is None:
                    return
                
                self.model.excluir_autor(idautor)
                mensagem("Autor excluído com sucesso!")
        except Exception as e:
            mensagem(f"Erro ao excluir autor: {e}")