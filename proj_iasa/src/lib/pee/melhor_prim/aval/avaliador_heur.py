from .avaliador import Avaliador

class AvaliadorHeur(Avaliador):

    def __init__(self):
        self.__heuristica = None
    
    @property
    def heuristica(self):
        return self.__heuristica
    
    @heuristica.setter
    def heuristica(self, heuristica):
        self.__heuristica = heuristica