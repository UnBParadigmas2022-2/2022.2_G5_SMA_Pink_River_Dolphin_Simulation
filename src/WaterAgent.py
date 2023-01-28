from src.PinkDolphinAgent import PinkDolphinAgent


class WaterAgent(PinkDolphinAgent):
    breed = "Agua"
    energy = 22
    moore = True
    radius = 3
    walk_radius = 2
    energy_loss = 2

    def __init__(self, unique_id, model):
        super().__init__(
            unique_id,
            model,
            self.breed,
            self.energy,
            self.moore,
            self.radius,
            self.walk_radius,
            self.energy_loss,
        )
