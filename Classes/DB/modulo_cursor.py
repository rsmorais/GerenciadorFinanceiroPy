from Classes.Util.module_utils import ModuleUtils as ModUtils
import sqlite3

class ModuloCursor():
	
	def __init__(self):
		varModUtils = ModUtils()
		self.db = varModUtils.get_db()

	def retrieve(self, sql, arg):
		conn = sqlite3.connect(self.db)
		cursor = conn.cursor()
		self.sql = sql
		if(arg != None):
			self.sql = sql.format(*arg)
		cursor.execute(self.sql)
		
		print('Dados recuperados com sucesso.')
		retorno = cursor.fetchall()
		conn.close()
		return retorno


