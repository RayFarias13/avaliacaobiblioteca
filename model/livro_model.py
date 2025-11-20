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
            cursor.execute("INSERT INTO livro (titulo, ano_publicacao, id_autor) VALUES (%s, %s, %s)",(titulo, ano_publicacao, autor_id),)
            self.conexao.commit()
            cursor.close()

        except Exception as e:
            print("Erro ao adicionar livro:", e)
            self.conexao.rollback()

    def listar_livros(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT * FROM livro INNER JOIN autor ON livro.id_autor = autor.id_autor")
            livros = cursor.fetchall()
            cursor.close()
            return livros
        
        except Exception as e:
            print("Erro ao listar livro(s):", e)
            return []
        
    def atualizar_livro(self, livro_id, titulo, ano_publicacao, autor_id):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("UPDATE livro SET titulo = %s, ano_publicacao = %s, id_autor = %s WHERE id_livro = %s", (titulo, ano_publicacao, autor_id, livro_id),)
            self.conexao.commit()
            cursor.close()

        except Exception as e:
            print("Erro ao atualizar livro:", e)
            self.conexao.rollback()
    
    def excluir_livro(self, livro_id):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM livro WHERE id_livro = %s", (livro_id,),)
            self.conexao.commit()
            cursor.close()

        except Exception as e:
            print("Erro ao excluir livro:", e)
            self.conexao.rollback()


        
    