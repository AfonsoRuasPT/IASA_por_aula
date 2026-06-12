from .passo_solucao import PassoSolucao

class Solucao:

    def __init__(self, no_final):
        self.__dimensao = no_final.profundidade
        self.__custo = no_final.custo
        self.__passo = []
        while no.antecessor: 
            passo = PassoSolucao(no.antecessor.estado,no.operador) 
            self.__passos.insert(0,passo) 
            no = no.antecessor 
    

    def __iter__(self): #iteravel 
        return iter(self.__passos)

    def __getitem__(self, index): # indexavel
        return self.__passos[index]


    @property
    def simensao(self):
        return self.__dimensao
    
    @property
    def custo(self):
        return self.__custo
    



