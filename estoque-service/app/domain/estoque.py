class Estoque:
    def __init__(self, produto):
        self.produto = produto

    def adicionar(self, quantidade):
        self.produto.quantidade += quantidade

    def remover(self, quantidade):
        if quantidade > self.produto.quantidade:
            raise ValueError("Estoque insuficiente")
        self.produto.quantidade -= quantidade

    def saldo(self):
        return self.produto.quantidade
