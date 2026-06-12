from .procura_informada import ProcuraInformada
from .aval.avaliador_sofrega import AvaliadorSofrega

class ProcuraSofrega(ProcuraInformada):

    def __init__(self):
        super().__init__(AvaliadorSofrega())
