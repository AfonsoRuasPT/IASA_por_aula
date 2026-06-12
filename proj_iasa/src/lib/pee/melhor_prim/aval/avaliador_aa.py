from .avaliador_heur import AvaliadorHeur

class AvaliadorAA(AvaliadorHeur):

    def prioridade(self, no):
        return self.heuristica.h(no.estado) + no.custo # f(n) = h(n) (heuristica) + g(h) (custo do nó)