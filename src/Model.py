import uuid
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa import Model
from src.PinkDolphinAgent import PinkDolphinAgent
from src.ShoalAgent import ShoalAgent
from src.WaterAgent import WaterAgent
from src.Poluente import Poluente
from src.FisherAgent import FisherAgent

class Model(Model):
    def __init__(self, num_dolphin,num_agents,num_poluentes,  width = 25, height = 25):
        self.num_agents = num_agents
        self.num_dolphin = num_dolphin
        self.grid = MultiGrid(width, height, True)
        self.width = width
        self.height = height
        self.schedule = RandomActivation(self)
        self.running = True
        self.steps = 0
        self.numero_poluentes = num_poluentes
        self.init_agent(PinkDolphinAgent, self.num_dolphin)
        self.init_agent(ShoalAgent, self.num_agents)
        self.init_agent(Poluente, self.numero_poluentes)
        self.init_agent(FisherAgent, 1)
        self.init_water(WaterAgent)

    def init_water(self,Agent):
        cont = 0
        for x in range(self.height):
            for y in range(self.width):
                id = uuid.uuid1()
                agent = Agent(id, self)
                if self.grid.is_cell_empty((x,y)):
                    cont+=1
                    self.schedule.add(agent)
                    self.grid.place_agent(agent,(x,y))

        #print(cont)
        #print(self.height*self.width)
        #print(self.height*self.width - cont)

    def init_agent(self, Agent, num_agents):
        #print("funcionou", Agent)
        for i in range(num_agents):
            id = uuid.uuid1()
            agent = Agent(id, self)
            self.schedule.add(agent)
            if self.grid.exists_empty_cells():
                #print("entrou")
                self.grid.place_agent(agent, self.grid.find_empty())

    def step(self):
        self.schedule.step()

    def reset_steps(self):
        self.steps = 0
        self.init_agent(ShoalAgent, self.num_agents)
        self.init_agent(FisherAgent, self.num_agents)

    def cria_boto(self):
        id = uuid.uuid1()
        agent = PinkDolphinAgent(id, self)
        self.schedule.add(agent)
        if self.grid.exists_empty_cells():
            #print("entrou")
            self.grid.place_agent(agent, self.grid.find_empty())
