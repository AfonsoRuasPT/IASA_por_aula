class Resposta:

    # Define uma resposta a estímulos, em termos de acção a realizar e da respectiva prioridade

    def __init__(self, accao):
        self._accao = accao # protected

    def activar(self, percepcao, intencidade = 0): # retorna accao
        if self._obter_accao is not None:
            self._accao.prioridade(intencidade)
        return self._accao # retorna a accao

    def _obter_accao(self, percepcao): # retorna a accao
        return self._accao