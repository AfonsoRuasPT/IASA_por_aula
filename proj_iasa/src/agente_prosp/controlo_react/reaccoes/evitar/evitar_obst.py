from lib.ecr.reaccao import Reaccao

class EvitarObst(Reaccao):
    """
    Evitar obstaculo é issencioal para o bom funcionamento e para a continuidade do jogo por issp tera uma hirarquia media ficando
    no meio de AproximarAlvo e Explorar
    Este comportamento deve verificar a distancia que esta de cada obstaculo, se essa distancia for irgual a 1 o agente deve rodar 90
    graus para a esquerda ou para a direita, com o conhecimento de que se ao rodar se depara com outro obstaculo deve rodar 
    para o mesmo lado
    """