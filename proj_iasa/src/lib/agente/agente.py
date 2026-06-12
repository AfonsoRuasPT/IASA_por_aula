from abc import abstractmethod, ABC

class Agente(ABC):

    def __init__(self, controlo):
        self._controlo = controlo

    @abstractmethod
    def _percepcionar(self):
        """Obter percepção do ambiente. Retorna uma percepção"""

    @abstractmethod
    def _actuar(self, accao):
        """Actua"""


    def executar(self):
        percepcao = self._percepcionar() # obtém percepção do ambiente chamando o método abstracto da subclasse
        accao = self._controlo.processar(percepcao) # delega a decisão ao Controlo, padrão de delegação: Agente utiliza Controlo processar, mantendo acoplamento baixo
        if accao is not None: # None é o valor que indica ausência de acção; usa-se "is not None" em vez de "!= None" porque é uma comparação de identidade (é o mesmo objecto None), não de valor
            return self._actuar(accao) # executa a acção concreta na subclasse
        return None # sem acção válida, o ciclo termina sem efeito

        """Executar acção no ambiente. Falta implementar o método executar da Classe Agente"""
        # raise NotImplementedError para dar erro caso o método seja chamado sem ser implementado
