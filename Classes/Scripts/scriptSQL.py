class RecuperaTLA:
	def get_sql(self):
		return """select TLA_idTipoLancamento,
			TLA_dsTipoLancamento,
			TLA_dtAtualizacao
			from TLA_TipoLancamento
			where TLA_dsTipoLancamento like '{0}'
			"""

class RecuperaCRT:
	def get_sql(self):
		return """select CRT_idCartao,
			CRT_dsCartao,
			CRT_dtVencimento,
			CRT_dtFechamento,
			CRT_nmUsuario,
			CRT_dtAtualizacao
			from CRT_Cartao
			where CRT_dsCartao like '{0}'
			"""