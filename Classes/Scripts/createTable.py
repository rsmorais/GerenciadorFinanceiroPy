import sqlite3

# conectando...
conn = sqlite3.connect('Financeiro.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
create table TLA_TipoLancamento(
	TLA_idTipoLancamento INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	TLA_dsTipoLancamento VARCHAR(40) not null,
	TLA_nmUsuario VARCHAR(20),
	TLA_dtAtualizacao DATE
);

""")
cursor.execute("""
create table FPG_FormaPagamento(
	FPG_idFormaPagamento INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	FPG_dsFormaPagamento VARCHAR(40) not null,
	FPG_nmUsuario VARCHAR(20),
	FPG_dtAtualizacao DATE
);
""")
cursor.execute("""
create table CRT_Cartao(
	CRT_idCartao INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	CRT_dsCartao VARCHAR(40) not null,
	CRT_dtVencimento DATE,
	CRT_dtFechamento DATE,
	CRT_nmUsuario VARCHAR(20),
	CRT_dtAtualizacao DATE
);
""")
cursor.execute("""
create table LNC_Lancamento(
	LNC_idLancamento INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
	LNC_dsLancamento VARCHAR(40) not null,
	LNC_dtLancamento DATE,
	LNC_dtAtualizacao DATE,
	LNC_nmUsuario VARCHAR(20),
 	LNC_idTipoLancamento INTEGER not null,
	LNC_idFormaPagamento INTEGER not null,
	LNC_idCartao INTEGER,
 	LNC_vlLancamento DECIMAL,
	foreign key (LNC_idTipoLancamento) references TLA_TipoLancamento(TLA_idTipoLancamento),
	foreign key (LNC_idCartao) references CRT_Cartao(CRT_idCartao),
	foreign key (LNC_idFormaPagamento) references FPG_FormaPagamento(FPG_idFormaPagamento)
);

""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()
