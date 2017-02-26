class RecuperaTLA:
	def get_sql(self):
		return """select TLA_idTipoLancamento,
			TLA_dsTipoLancamento,
			TLA_nmUsuario,
			TLA_dtAtualizacao
			from TLA_TipoLancamento"""