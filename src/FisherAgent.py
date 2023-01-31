from mesa import Agent
from src.PinkDolphinAgent import PinkDolphinAgent
from src.WaterAgent import WaterAgent


class FisherAgent(Agent):
    grid = None
    moore = None
    radius = None
    walk_radius = None
    food = None

    def __init__(
        self,
        unique_id,
        model,
        breed="Boto",
        moore=True,
        radius=3,
        walk_radius=1,
    ):
        super().__init__(unique_id, model)
        self.moore = moore
        self.radius = radius
        self.walk_radius = walk_radius
        self.food = 0

    def step(self):
        try:
            self.walk_search_food()
            self.verifica_pos_boto(PinkDolphinAgent)
        except:
            pass

    def walk_search_food(self):
        possible_walk_pos = self.model.grid.get_neighborhood(
            self.pos, moore=self.moore, radius=self.radius
        )
        new_position = self.get_new_position(possible_walk_pos, self.pos)

        self.model.grid.move_agent(self, new_position)

    def get_new_position(self, possible_walk_pos, current_pos):
        next_pos = None
        current_best_pos = None
        minimum_distance = 10**6
        step_x = 0
        step_y = 0

        for walk_pos in possible_walk_pos:
            food = self.get_food_agent(walk_pos)
            if len(food) > 0:
                current_distance = (current_pos[0] - walk_pos[0]) ** 2 + (
                    current_pos[1] - walk_pos[1]
                ) ** 2
                if current_distance < minimum_distance:
                    minimum_distance = current_distance
                    current_best_pos = walk_pos

        if current_best_pos != None:
            if current_pos[0] < current_best_pos[0]:
                step_x = 1
            elif current_pos[0] > current_best_pos[0]:
                step_x = -1

            if current_pos[1] < current_best_pos[1]:
                step_y = 1
            elif current_pos[1] > current_best_pos[1]:
                step_y = -1

            next_pos = (
                current_pos[0]
                + min(self.walk_radius, abs(current_pos[0] - current_best_pos[0]))
                * step_x,
                current_pos[1]
                + min(self.walk_radius, abs(current_pos[1] - current_best_pos[1]))
                * step_y,
            )

            return next_pos

        next_pos = self.model.grid.get_neighborhood(
            self.pos, moore=self.moore, include_center=False, radius=self.walk_radius
        )
        return self.random.choice(next_pos)

    def verifica_pos_boto(self, agent_type):
        for agent in self.model.grid.get_cell_list_contents([self.pos]):
            if type(agent) is agent_type and agent != self:
                self.model.grid.remove_agent(agent)

    def get_food_agent(self, pos):
        try:
            this_cell = self.model.grid.get_cell_list_contents([pos])
            return [obj for obj in this_cell if not isinstance(obj, WaterAgent)]
        except:
            return []
