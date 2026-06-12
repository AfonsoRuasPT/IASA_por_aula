from lib.ecr.accao import Accao
from lib.sae.agente.movimento import Movimento

class Avancar(Movimento, Accao):
    
    def __init__(self):
        super().__init__(None, 1) # chama o construtor da classe Movimento, com direcao None (direção que ja estava) e passo de 1 unidade
