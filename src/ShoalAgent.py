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
                self.analyze_water_quality()
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

    def analyze_water_quality(self):
        try:
            next_pos = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False, radius=1)
            next_pos_content = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False, radius=1)
            highest_quality_cell = [None, 0]
            for idx, cell in enumerate(next_pos_content):
                if isinstance(cell, WaterAgent):
                    if cell.qualidade >= highest_quality_cell[1]:
                        highest_quality_cell = [idx, cell.qualidade]
            if highest_quality_cell != [None, 0]:
                print(next_pos[highest_quality_cell[0]])
                self.model.grid.move_agent(self, next_pos[highest_quality_cell[0]])

        except:
            print('error when calling analyze_water_quality')