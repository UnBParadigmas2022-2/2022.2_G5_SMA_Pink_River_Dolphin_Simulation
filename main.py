from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from src.ShoalAgent import ShoalAgent
from src.PinkDolphinAgent import PinkDolphinAgent
from src.WaterAgent import WaterAgent
from src.Model import Model


def portrayal_method(agent):
    portrayal = {
        "Filled": "true", 
        "Layer": 0, 
        "w": 1, 
        "h": 1,
    }

    if type(agent) is ShoalAgent:
        if not agent.eated:
            portrayal["Shape"] = "assets/cardume.png"

    elif type(agent) is PinkDolphinAgent:
        portrayal["Shape"] = "assets/pink_dolphin.jpg"

    elif type(agent) is WaterAgent:
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "blue"
    return portrayal


grid = CanvasGrid(portrayal_method, 15, 15, 550, 550)
server = ModularServer(
    Model, [grid], "Pink Dolphin", {"num_agents": 25, "width": 15, "height": 15}
)
server.port = 8001
server.launch()
