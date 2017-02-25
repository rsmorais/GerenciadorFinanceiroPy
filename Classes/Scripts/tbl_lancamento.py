import sqlite3

conn = sqlite3.connect('Financeiro.db')
cursor = conn.cursor()

# criando uma lista de dados
lista = [('Lazer', 'rafael', '2017-02-23'),
    ('Alimentação', 'rafael', '2017-02-23'),
    ('Vestuário', 'rafael', '2017-02-23'),
    ('Saúde', 'rafael', '2017-02-23'),
    ('Estudo', 'rafael', '2017-02-23')]
    
# inserindo dados na tabela
cursor.executemany("""
INSERT INTO TLA_TipoLancamento (TLA_dsTipoLancamento, TLA_nmUsuario, TLA_dtAtualizacao)
VALUES (?, ?, ?)
""", lista)

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
