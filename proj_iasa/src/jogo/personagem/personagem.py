from agente.agente_jogo import AgenteJogo
from .controlo_personagem import ControloPersonagem


class Personagem(AgenteJogo):

    def __init__(self, ambiente):
        super().__init__(ambiente, ControloPersonagem()) 
    
    def mostrar(self):
        print(f"\nPersonagem: {self._controlo._maq_est.estado_atual.name}")