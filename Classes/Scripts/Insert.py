import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# inserindo dados na tabela
cursor.execute("""
INSERT INTO Lancamento (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Regis', 35, '00000000000', 'regis@email.com', '11-98765-4321', 'Sao Paulo', 'SP', '2014-06-08')
""")

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
