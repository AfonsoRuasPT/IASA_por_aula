from lib.ecr.hierarquia import Hierarquia

class Recolher(Hierarquia):

    """
    Recolher é um comportamento composto, cuja selecao de accao é feita de forma hierarquica.
    Este comportamento composto, é composto por 3 comportamentos: AproximarAlvo, EviarObst, Explorar.
    A hierarquia de cad acomportamento está descrito em cada um deles
    """

    """"""