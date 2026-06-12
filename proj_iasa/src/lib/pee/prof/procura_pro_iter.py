from .procura_prof_lim import ProcuraProfLim

class ProcuraProIter(ProcuraProfLim):

    def procurar(self, problema, inc_prof=1, limite_prof=100):
        for prof_max in range(0, limite_prof + 1, inc_prof):
            solucao = super().procurar(problema, prof_max) 
            if solucao:
                return solucao