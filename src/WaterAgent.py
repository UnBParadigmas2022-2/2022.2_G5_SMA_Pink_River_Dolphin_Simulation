from mesa import Agent

class WaterAgent(Agent):

    def __init__(self, unique_id, model,temperatura = 20,qualidade = 5):
        super().__init__(unique_id,model)
        self.temperatura = temperatura,
        self.qualidade = qualidade
    
    def perdeQualidade(self):
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
    
    
