from ..mec_proc.fronteira import Fronteira
from heapq import heappush, heappop

class FronteiraPrioridade(Fronteira):

    def __init__(self, avaliador):
        super().__init__()
        self.__avaliador = avaliador

    def inserir(self, no):
        no.prioridade = self.__avaliador.prioridade(no)
        heappush(self.nos, no)

    def remover(self):
        return heappop(self.nos)