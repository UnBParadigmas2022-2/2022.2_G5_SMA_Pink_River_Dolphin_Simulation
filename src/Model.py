import uuid
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa import Model
from src.PinkDolphinAgent import PinkDolphinAgent
from src.ShoalAgent import ShoalAgent
from src.WaterAgent import WaterAgent


class Model(Model):
    def __init__(self, num_agents, width = 15, height = 15,):
        self.num_agents = num_agents
        self.grid = MultiGrid(width, height, True)
        self.width = width
        self.height = height
        self.schedule = RandomActivation(self)
        self.running = True
        self.steps = 0
        self.init_agent(PinkDolphinAgent, 5)
        self.init_agent(ShoalAgent, self.num_agents)
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

        print(cont)
        print(self.height*self.width)
        print(self.height*self.width - cont)

    def init_agent(self, Agent, num_agents):
        for i in range(num_agents):
            id = uuid.uuid1()
            agent = Agent(id, self)
            self.schedule.add(agent)
            if self.grid.exists_empty_cells():
                self.grid.place_agent(agent, self.grid.find_empty())

    def step(self):
        if self.steps == 10:
            self.reset_steps()
        else:
            self.steps += 1

        self.schedule.step()

    def reset_steps(self):
        self.steps = 0
        self.init_agent(ShoalAgent, self.num_agents)

    

    
