from app.strategies.validacao import ValidacaoMovimentacao

class ValidacaoPadrao(ValidacaoMovimentacao):

    def validar(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
