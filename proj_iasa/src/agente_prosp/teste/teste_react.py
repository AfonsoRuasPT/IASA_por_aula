from agente_prosp.controlo_react.reaccoes.explorar.explorar import Explorar
from agente_prosp.controlo_react.controlo_react import ControloReact
from agente_prosp.agente_prosp import AgenteProsp
from sae import Simulador

# criar uma instancia de agente prosp que internamente tem um controlo reactivo com um comportamento de instancia explorar

"""
AgenteProsp não tem construtor, mas herda de Agente que recebe como parametro um controlo, ControloReact é um controlo.
O controlo tem como parametros um comportamento, e Ecplorar é um comportamento.
"""


if __name__ == "__main__":

    comportamento = Explorar() # intanciar o comportamento Explorar
    controlo = ControloReact(comportamento) # intanciar o controlo ControloReact com o comportamento
    agente = AgenteProsp(controlo) # instanciar o agente AgenteProsp com o controlo
    simulador = Simulador(2, agente)
    simulador.executar()