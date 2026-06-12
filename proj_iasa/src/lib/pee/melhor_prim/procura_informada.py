from .procura_melhor_prim import ProcuraMelhorPrim

class ProcuraInformada(ProcuraMelhorPrim):

    def procurar(self, problema, heuiristica):
        self._avaliador.heuiristica = heuiristica
        super().procurar(problema)