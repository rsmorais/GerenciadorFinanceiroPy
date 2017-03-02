from Classes.Util.module_utils import ModuleUtils as ModUtils
import sqlite3

class TBL_CRT_Cartao():
	
	def __init__(self):
		varModUtils = ModUtils()
		self.db = varModUtils.get_db()
		self.data = varModUtils.get_date()
		self.usuario  = varModUtils.get_user()
               
	def insert(self, lista):
		print('insert CRT')
		# conectando no *.db
		conn = sqlite3.connect(self.db)
		cursor = conn.cursor()

		for linha in lista:
			print(linha)
			# inserindo dados na tabela
			cursor.executemany("""
				INSERT INTO CRT_Cartao (CRT_dsCartao, CRT_dtVencimento, CRT_dtFechamento, CRT_nmUsuario, CRT_dtAtualizacao)
				VALUES (?, ?, ?, ?, ?)
				""", [(linha['CRT_dsCartao'], linha['CRT_dtVencimento'], linha['CRT_dtFechamento'], self.usuario, self.data)])
		
		# gravando no bd
		conn.commit()
		conn.close()
		print('Dados inseridos com sucesso.')
		
	def delete(self, lista):
		print('delete CRT')
		# conectando no *.db
		conn = sqlite3.connect(self.db)
		cursor = conn.cursor()

		for linha in lista:
			print(linha)
			# deletando dados na tabela
			cursor.executemany("""
				DELETE FROM CRT_Cartao
				WHERE CRT_idCartao = ?
				""", [(linha['CRT_idCartao'],)])
			
		# gravando no bd
		conn.commit()
		conn.close()
		print('Dados deletados com sucesso.')
				
	def edit(self, lista):
		print('edit CRT')
		# conectando no *.db
		conn = sqlite3.connect(self.db)
		cursor = conn.cursor()

		for linha in lista:
			# editando dados na tabela
			cursor.executemany("""UPDATE CRT_Cartao
				SET CRT_dsCartao = ?, CRT_dtVencimento = ?, CRT_dtFechamento = ?, CRT_nmUsuario = ?, CRT_dtAtualizacao = ?
				WHERE  CRT_idCartao = ?
				""", [(linha['CRT_dsCartao'], linha['CRT_dtVencimento'], linha['CRT_dtFechamento'], self.usuario, self.data, linha['CRT_idCartao'])])
		
		# gravando no bd
		conn.commit()
		conn.close()
		print('Dados atualizados com sucesso.')

