from mesa import Agent


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
        radius=3,
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

    def step(self):
        try:
            self.energy -= self.energy_loss
            self.walk_search_food()
            self.check_got_food(2)
            self.check_got_energy()
        except:
            pass

    def walk_search_food(self):
        possible_walk_pos = self.model.grid.get_neighborhood(
            self.pos, moore=self.moore, include_center=True, radius=self.radius
        )
        new_position = self.get_new_position(possible_walk_pos, self.pos)
        self.model.grid.move_agent(self, new_position)
        print(format(self.breed), "Procurar cardume")

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

    def get_food_agent(self, pos):
        try:
            this_cell = self.model.grid.get_cell_list_contents([pos])
            return [obj for obj in this_cell if not isinstance(obj, PinkDolphinAgent)]
        except:
            return []

    def check_got_food(self, min_to_reproduce):
        if self.model.steps + 1 == 10:
            if self.food >= min_to_reproduce:
                if self.breed == "Boto":
                    self.model.init_agent(PinkDolphinAgent, 2)
                elif self.breed == "Agua":
                    from WaterAgent import WaterAgent

                    self.model.init_agent(WaterAgent, 2)
                self.food = 0
            if self.food == 0:
                self.energy = 0

    def check_got_energy(self):
        if self.energy == 0:
            self.model.grid.remove_agent(self)
