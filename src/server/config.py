from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer


class Configuration():
    server = None
    grid = None
    grid_width = None
    grid_height = None
    canvas_width = None
    canvas_height = None
    server_port = None
    number_of_agents = None

    def __init__(
        self,
        grid_width, 
        grid_height, 
        canvas_width, 
        canvas_height, 
        server_port, 
        number_of_agents
    ):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.server_port = server_port
        self.number_of_agents = number_of_agents

    def configure_grid(self):
        self.grid = CanvasGrid(
            None, # Precisamos colocar aqui o nome da função portrayal_method
            self.grid_width, 
            self.grid_height, 
            self.canvas_width, 
            self.canvas_height
        )

    def configure_server(self):
        self.server = ModularServer(
            None, # Precisamos colocar aqui o nome da classe do modelo
            [self.grid], 
            "Pink Dolphin", 
            {
               """ Precisamos colocar aqui os argumentos para a 
               classe do modelo, como a quantidade de agentes e
               a altura e largura que eles estarão no mapa """
            },
            self.server_port
        )

    def run_server(self):
        self.server.launch()
