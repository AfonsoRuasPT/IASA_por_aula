from mod import Estado, Operador

class PassoSolucao(Estado, Operador):

    def __init__(self, estado, operador):
        self.__estado = estado
        self.__operador = operador

    @property #objeto imutavel, nao pode ser alterado depois de criado
    def estado(self):
        return self.__estado
    
    @property #objeto imutavel, nao pode ser alterado depois de criado
    def operador(self):
        return self.__operador

    