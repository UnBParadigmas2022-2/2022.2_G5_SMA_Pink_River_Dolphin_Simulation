from mesa import Agent
from src.WaterAgent import WaterAgent
from src.ShoalAgent import ShoalAgent

import random

class PinkDolphinAgent(Agent):
    breed = None
    energy = None
    grid = None
    moore = None
    radius = None
    walk_radius = None
    energy_loss = None
    food = None

    def __init__(
        self,
        unique_id,
        model,
        breed="Boto",
        energy=20,
        moore=True,
        radius=1,
        walk_radius=1,
        energy_loss=1,
    ):
        super().__init__(unique_id, model)
        self.breed = breed
        self.energy = energy
        self.moore = moore
        self.radius = radius
        self.walk_radius = walk_radius
        self.energy_loss = energy_loss
        self.food = 0
        self.pre = self.pos
        self.fugindo = False

    def step(self):
        try:
            self.energy -= self.energy_loss
            self.procura_shoal()
            self.analise_de_energia_botonica()
            #self.procura_bobby_fisher()
            self.analise_agua()
            self.procura_food()
        except:
            pass
    
    def get_good_pos(self):
        possible = self.model.grid.get_neighbors(self.pos,moore = True)
        self.random.shuffle(possible)

        for agent in possible:
            if type(agent) is WaterAgent:
                #print('LIMPAAAA')
                if agent.qualidade > 2:
                    return agent.pos

    def migrate(self):
        #print("-------MIGRATEEEEEE---------")
        self.fugindo = True
        rand_pos = self.get_good_pos()
        #print(f"###### RAND {rand_pos} SELFPOS {self.pos} PRE {self.pre}")
        pre = self.pre
        if rand_pos != pre:
            #print("NO ESCURINHO DO CINEMA")
            self.pre = self.pos
            self.model.grid.move_agent(self,rand_pos)
        # escolhe uma aleatório que não seja a pre

    def analise_agua(self):
        if self.get_water_quality():
            self.migrate()

    def get_water_quality(self):
        for agent in self.model.grid.get_neighbors(self.pos,moore = True,include_center = True):
            if type(agent) is WaterAgent:
                if agent.qualidade <= 2:
                    # água ruim MIGRA
                    return True
        return False

    def analise_de_energia_botonica(self):
        if self.energy <= 10:
            # com fome, procura comida.
            self.migrate()
    
    def procura_bobby_fisher(self):
        for agent in self.model.grid.get_neighbors(self.pos,moore = True,include_center = True):
            if type(agent) is FisherAgent:
                # pescador perto MIGRA
                self.migrate()

    def procura_shoal(self): 
        for agent in self.model.grid.get_neighbors(self.pos,moore = True):
            if type(agent) is ShoalAgent:
                print("NO ESCURINHO DO GOLFINHO")
                print(agent.pos)
                self.model.grid.move_agent(self,agent.pos)
                agent.come()
                self.energy+=5

    def random_walk(self):
        pass            

    # função boa, do grupo do formigueiro de 2021.2, mas ainda não usada
    def get_item(self, agent_type):
        for agent in self.model.grid.get_cell_list_contents([self.pos]):
            if type(agent) is agent_type and agent != self:
                return agent

