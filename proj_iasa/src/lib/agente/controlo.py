from abc import ABC, abstractmethod

class Controlo(ABC):


    @abstractmethod
    def processar(self, percepcao):
        """Processar a percepção e retornar uma acção. Falta implementar o método processar da Interface Controlo"""
