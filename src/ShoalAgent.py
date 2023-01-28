from mesa import Agent


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
