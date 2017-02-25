import sqlite3

class TBL_TLA_TipoLancamento():
	
	def __init__(self):
		self.db = 'Financeiro.db'
               
	def inserir(self, lista):
		# conectando no *.db
		conn = sqlite3.connect(self.db)
		cursor = conn.cursor()
		
		# inserindo dados na tabela
		cursor.executemany("""
			INSERT INTO TLA_TipoLancamento (TLA_dsTipoLancamento, TLA_nmUsuario, TLA_dtAtualizacao)
			VALUES (?, ?, ?)
			""", lista)
		
		# gravando no bd
		conn.commit()
		conn.close()
		print('Dados inseridos com sucesso.')
		
	def excluir(self, lista):
		pass
		
	def editar(self, lista):
		pass

