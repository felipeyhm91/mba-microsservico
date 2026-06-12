from abc import ABC, abstractmethod

class ValidacaoMovimentacao(ABC):

    @abstractmethod
    def validar(self, quantidade):
        pass
