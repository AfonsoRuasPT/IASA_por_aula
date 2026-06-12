from jogo.agente.agente_jogo import AgenteJogo
from jogo.personagem.controlo_personagem import ControloPersonagem


class Personagem(AgenteJogo):

    def __init__(self, ambiente):
        super().__init__(ambiente, ControloPersonagem()) 
    
    def mostrar(self):
        """"""