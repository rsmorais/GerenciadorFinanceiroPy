from Classes.Util.module_utils import ModuleUtils as ModUtils
import sqlite3

class TBL_TLA_TipoLancamento():
	
	def __init__(self):
		varModUtils = ModUtils()
		self.db = varModUtils.get_db()
		self.data = varModUtils.get_date()
		self.usuario  = varModUtils.get_user()
               
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
				""", [(linha['TLA_idTipoLancamento'],)])
			
		# gravando no bd
		conn.commit()
		conn.close()
		print('Dados deletados com sucesso.')
				
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

