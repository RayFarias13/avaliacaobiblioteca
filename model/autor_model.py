import psycopg2

class AutorModel:
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

    def cadastrar_autor(self, nome, nacionalidade):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO autor (nome, nacionalidade) VALUES (%s, %s)", (nome, nacionalidade),)
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("Erro ao adicionar autor:", e)
            self.conexao.rollback()

    def listar_autores(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT * FROM autor ORDER BY id_autor") 
            autores = cursor.fetchall()
            cursor.close()
            return autores
        except Exception as e:
            print("Erro ao listar autores:", e)
            return []

    def atualizar_autor(self, autor_id, nome, nacionalidade):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("UPDATE autor SET nome = %s, nacionalidade = %s WHERE id_autor = %s", (nome, nacionalidade, autor_id),)
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("Erro ao atualizar autor:", e)
            self.conexao.rollback()

    def excluir_autor(self, autor_id):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM autor WHERE id_autor = %s", (autor_id,),)
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("Erro ao excluir autor (Verifique se ele possui livros vinculados):", e)
            self.conexao.rollback()