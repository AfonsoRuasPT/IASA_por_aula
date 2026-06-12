from .avaliador_heur import AvaliadorHeur

class AvaliadorSofrega(AvaliadorHeur):

    def prioridade(self, no):
        return self.heuristica.h(no.estado) # f(n) = h(n)