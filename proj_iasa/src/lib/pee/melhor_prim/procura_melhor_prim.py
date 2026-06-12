from ..mec_proc.procura_grafo import ProcuraGrafo
from .fronteira_prioridade import FronteiraPrioridade

class ProcuraMelhorPrim(ProcuraGrafo):

    def __init__(self, avaliador):
        super().__init__(FronteiraPrioridade(avaliador))
        self._avaliador = avaliador


    def _manter(self, no):
        return super()._manter(no) or no.custo < self._explorados[no.estado].custo 
    # o nó tambem se mantem se o custo desse nó for inferior ao custo do nó na lista explorados