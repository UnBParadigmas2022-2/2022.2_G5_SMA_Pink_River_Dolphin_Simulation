import mesa
from mesa import Agent
from src.Poluente import Poluente


class WaterAgent(Agent):
    def __init__(self, unique_id, model,temperatura = 20,qualidade = 5):
        super().__init__(unique_id,model)
        self.temperatura = temperatura,
        self.qualidade = qualidade
        self.count = 0
    
    def step(self):
        self.count+=1
        if self.count % 5 == 0:
            try:
                self.procuraPoluente()
            except:
                pass

    def perdeQualidade(self):
        print("Perdi")
        if self.qualidade > 1:
            self.qualidade -= 1
        
        return self.qualidade
    
    def aumentaQualidade(self):
        self.qualidade += 1
        return self.qualidade
    
    def aumentaTemperatura(self):
        self.temperatura += 5
        return self.temperatura
    
    def diminuiTemperatura(self):
        self.temperatura -= 5
        return self.temperatura
    
    def procuraPoluente(self):
        for agent in self.model.grid.get_neighbors(self.pos,moore = False):
            if type(agent) is Poluente:
                self.perdeQualidade()
            
            if agent.qualidade < 3:
                self.perdeQualidade()

