import psycopg2

class LivroModel:
    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
                host="ep-small-bread-acdziraa-pooler.sa-east-1.aws.neon.tech",
                database="neondb",
                user="neondb_owner",
                password="npg_svwb7DQBh5ku",
                port="5432",
                sslmode="require",
                channel_binding=None,
            )

        except Exception as e:
            print("Erro ao conectar ao banco:", e)

    def cadastrar_livro(self,titulo,ano_publicacao,autor_id):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO livros (titulo, ano_publicacao, autor_id) VALUES (%s, %s, %s)",(titulo, ano_publicacao, autor_id),)
            self.conexao.commit()
            cursor.close()
            print("Livro adicionado com sucesso!")

        except Exception as e:
            print("Erro ao adicionar livro:", e)
            self.conexao.rollback()

    def listar_livros(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT * FROM livros")
            livros = cursor.fetchall()
            cursor.close()
            return livros
        
        except Exception as e:
            print("Erro ao listar livro(s):", e)
            return []
        
    def atualizar_livro(self, livro_id, titulo, ano_publicacao, autor_id):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("UPDATE livros SET titulo = %s, ano_publicacao = %s, autor_id = %s WHERE id = %s", (titulo, ano_publicacao, autor_id, livro_id),)
            self.conexao.commit()
            cursor.close()
            print("Livro atualizado com sucesso!")

        except Exception as e:
            print("Erro ao atualizar livro:", e)
            self.conexao.rollback()
    
    def excluir_livro(self, livro_id):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM livros WHERE id = %s", (livro_id,),)
            self.conexao.commit()
            cursor.close()
            print("Livro excluído com sucesso!")

        except Exception as e:
            print("Erro ao excluir livro:", e)
            self.conexao.rollback()


        
    