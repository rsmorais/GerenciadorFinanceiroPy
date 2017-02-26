import sqlite3

class ModuloCursor():
	
	def __init__(self):
		self.db = 'Financeiro.db'
		          
	def retrieve(self, sql, arg):
		conn = sqlite3.connect(self.db)
		cursor = conn.cursor()
		if(arg != None):
			cursor.execute(sql, arg)
		else:
			cursor.execute(sql)
		
		print('Dados recuperados com sucesso.')
		retorno = cursor.fetchall()
		conn.close()
		return retorno


