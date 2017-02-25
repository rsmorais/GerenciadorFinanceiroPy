create table TLA_TipoLancamento(
	TLA_idTipoLancamento int primary key,
	TLA_dsTipoLancamento varchar(40) not null
);

create table FPG_FormaPagamento(
	FPG_idFormaPagamento int primary key,
	FPG_dsFormaPagamento varchar(40) not null
);

create table CRT_Cartao(
	CRT_idCartao int primary key,
	CRT_dsCartao varchar(40) not null,
	CRT_dtVencimento date,
	CRT_dtFechamento date
);

create table LNC_Lancamento(
	LNC_idLancamento int primary key, 
	LNC_dsLancamento varchar(40) not null,
	LNC_dtLancamento date,
	LNC_dtAtualizacao date,
	LNC_idUsuario varchar(20),
 	LNC_idTipoLancamento int not null,
	LNC_idFormaPagamento int not null,
	LNC_idCartao int,
 	LNC_vlLancamento decimal,
	foreign key (LNC_idTipoLancamento) references TLA_TipoLancamento(TLA_idTipoLancamento),
	foreign key (LNC_idCartao) references CRT_Cartao(CRT_idCartao),
	foreign key (LNC_idFormaPagamento) references FPG_FormaPagamento(FPG_idFormaPagamento)
);

INSERT INTO TLA_TipoLancamento (TLA_dsTipoLancamento, TLA_nmUsuario, TLA_dtAtualizacao)
VALUES ('Lazer', 'rafael', '2017-02-23')

select *
from TLA_TipoLancamento
