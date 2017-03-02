import datetime

class ModuleUtils:
    def __init__(self):
        self.data = datetime.datetime.now()
        self.user = 'rafael'
        self.db = 'Banco/Financeiro.db'

    def get_date(self):        
        return self.data.date().strftime("%Y-%m-%d")

    def get_user(self):
        return self.user

    def get_db(self):
    	return self.db

