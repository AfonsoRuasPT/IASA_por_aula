from agente.accao import Accao


class AccaoJogo(Accao):

    def __init__(self, comando):
        self.__comando = comando # atributo privado (dois underscores "__")

    @property
    def comando(self):
        return self.__comando # devolve o ComandoJogo encapsulado
