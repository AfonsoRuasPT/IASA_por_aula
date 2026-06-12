from lib.agente.controlo import Controlo

class ControloReact(Controlo):

    def __init__(self, comportamento):
        self.__comportamento = comportamento

    def processar(self, percepcao): # retorna uma accao
        return self.__comportamento.activar(percepcao)