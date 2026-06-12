from .percepcao_jogo import PercepcaoJogo
from agente.agente import Agente

class AgenteJogo(Agente):

    def __init__(self, ambiente, controlo):
        super().__init__(controlo) # PYTHON – super().__init__: chama o construtor da super classe, classe pai
        # __init__(controlo) invoca o seu construtor para inicializar
        # o atributo protegido _controlo herdado. Sem esta chamada
        # _controlo não existiria e o método executar de Agente falharia.

        self.__ambiente = ambiente # atributo privado: AmbienteJogo; inacessível fora desta classe

    def _percepcionar(self):
        evento = self.__ambiente.observar() # chama o método público observar do AmbienteJogo para obter o evento actual
        return PercepcaoJogo(evento) # cria e devolve uma PercepcaoJogo encapsulando o evento; PercepcaoJogo realiza a interface Percepcao

    def _actuar(self, accao):
        self.__ambiente.executar(accao.comando) # acede ao ComandoJogo via propriedade pública "comando" de AccaoJogo e executa-o no ambiente