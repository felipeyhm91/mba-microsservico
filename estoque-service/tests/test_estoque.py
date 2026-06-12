import pytest
from app.domain.produto import Produto
from app.domain.estoque import Estoque

def test_entrada_estoque():
    produto = Produto(1, "Notebook", 10)
    estoque = Estoque(produto)
    estoque.adicionar(5)
    assert estoque.saldo() == 15

def test_saida_estoque():
    produto = Produto(1, "Notebook", 10)
    estoque = Estoque(produto)
    estoque.remover(3)
    assert estoque.saldo() == 7

def test_saida_maior_que_saldo():
    produto = Produto(1, "Notebook", 5)
    estoque = Estoque(produto)
    with pytest.raises(ValueError):
        estoque.remover(10)