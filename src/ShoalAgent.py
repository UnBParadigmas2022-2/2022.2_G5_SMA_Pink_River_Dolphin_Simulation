from mesa import Agent
from src.WaterAgent import WaterAgent


class ShoalAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.food = 1
        self.eated = False

    def step(self):
        try:
            self.give_food()
            if self.eated:
                self.model.grid.remove_agent(self)
            else:
                self.check_if_its_surrounded_by_polution()
                self.analyze_water_quality()
                # self.procuraLixo()
        except:
            pass

    def give_food(self):
        species = self.get_specie_agent(self.pos)
        if len(species) > 0:
            specie = species[0]
            specie.food += 1
            self.eated = True

    def get_specie_agent(self, pos):
        try:
            this_cell = self.model.grid.get_cell_list_contents([pos])
            return [obj for obj in this_cell if not isinstance(obj, ShoalAgent)]
        except:
            return []

    def check_if_its_surrounded_by_polution(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=False, include_center=False, radius=1)
        is_surrounded_by_polution = True
        for agent in neighbors:
            if type(agent) is WaterAgent:
                if agent.qualidade > 1:
                    is_surrounded_by_polution = False
        if is_surrounded_by_polution:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            self.model.init_agent(WaterAgent, 1)

    def analyze_water_quality(self):
        try:
            next_pos = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False, radius=1)
            next_pos_content = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False, radius=1)
            lowest_quality_cell = [None, 5]
            for idx, agent in enumerate(next_pos_content):
                if type(agent) is WaterAgent:
                    if agent.qualidade < lowest_quality_cell[1]:
                        lowest_quality_cell = [idx, agent.qualidade]
            if lowest_quality_cell[1] < 5:
                for idx, x in enumerate(next_pos_content):
                  if idx != lowest_quality_cell[0]:
                    self.model.grid.move_agent(next_pos_content[idx], self.pos)
                    self.model.grid.move_agent(self, next_pos[idx])
                    break
        except:
            pass
                