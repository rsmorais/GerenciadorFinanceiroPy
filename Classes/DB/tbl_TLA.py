import sqlite3

class TBL_TLA_TipoLancamento():
	
	def __init__(self):
		self.db = 'Financeiro.db'
		self.data = '2017-02-25'
		self.usuario  = 'rafael'
               
	def insert(self, lista):
		print('insert TLA')
		# conectando no *.db
		conn = sqlite3.connect(self.db)
		cursor = conn.cursor()

		for linha in lista:
			print(linha)
			# inserindo dados na tabela
			cursor.executemany("""
				INSERT INTO TLA_TipoLancamento (TLA_dsTipoLancamento, TLA_nmUsuario, TLA_dtAtualizacao)
				VALUES (?, ?, ?)
				""", [(linha['TLA_dsTipoLancamento'], self.usuario, self.data)])
		
		# gravando no bd
		conn.commit()
		conn.close()
		print('Dados inseridos com sucesso.')
		
	def delete(self, lista):
		print('delete TLA')
		# conectando no *.db
		conn = sqlite3.connect(self.db)
		cursor = conn.cursor()

		for linha in lista:
			print(linha)
			# deletando dados na tabela
			cursor.executemany("""
				DELETE FROM TLA_TipoLancamento
				WHERE TLA_idTipoLancamento = ?
				""", [(linha['TLA_idTipoLancamento'])])
			
		# gravando no bd
		conn.commit()
		conn.close()
		print('Dados inseridos com sucesso.')
				
	def edit(self, lista):
		print('edit TLA')
		# conectando no *.db
		conn = sqlite3.connect(self.db)
		cursor = conn.cursor()

		for linha in lista:
			# editando dados na tabela
			cursor.executemany("""UPDATE TLA_TipoLancamento 
				SET TLA_dsTipoLancamento = ?, TLA_nmUsuario = ?, TLA_dtAtualizacao = ?
				WHERE  TLA_idTipoLancamento = ?
				""", [(linha['TLA_dsTipoLancamento'], self.usuario, self.data, linha['TLA_idTipoLancamento'])])
		
		# gravando no bd
		conn.commit()
		conn.close()
		print('Dados atualizados com sucesso.')

app = TBL_TLA_TipoLancamento()
