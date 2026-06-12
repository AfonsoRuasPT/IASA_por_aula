from .mecanismo_procura import MecanismosProcrua

class ProcuraGrafo(MecanismosProcrua):

    def _iniciar_memoria(self):
        super()._iniciar_memoria() # invocar o iniciar memoria da super class para iniciar a fronteira
        self._explorados = {} # inicia o dicionario vazio dos explorados
        

    def _memorizar(self, no):
        # se for para manter o no, 
        if self._manter(no):
            self._explorados[no.estados] = no
            super()._memorizar(no)

    def _manter(self, no):
        return no.estado not in self._explorados