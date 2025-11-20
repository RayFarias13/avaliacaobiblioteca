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