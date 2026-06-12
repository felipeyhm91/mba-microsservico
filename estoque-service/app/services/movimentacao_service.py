class MovimentacaoService:

    def __init__(self, repository, notificacao, validacao):
        self.repository = repository
        self.notificacao = notificacao
        self.validacao = validacao

    def entrada(self, estoque, quantidade):
        self.validacao.validar(quantidade)
        estoque.adicionar(quantidade)
        self.repository.salvar(estoque)

    def saida(self, estoque, quantidade):
        self.validacao.validar(quantidade)
        estoque.remover(quantidade)
        self.repository.salvar(estoque)

        if estoque.saldo() < 5:
            self.notificacao.enviar_alerta("Estoque baixo")
