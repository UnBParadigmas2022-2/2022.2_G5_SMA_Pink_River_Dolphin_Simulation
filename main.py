from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from src.ShoalAgent import ShoalAgent
from src.PinkDolphinAgent import PinkDolphinAgent
from src.WaterAgent import WaterAgent
from src.Model import Model

descricao = "Seguindo a temática de animais em risco de extinção aplicada nas duas últimas entregas, \
decidimos desenvolver um sistema que simule as rotas migratórias do Boto Cor de Rosa, \
tendo como base determinadas complicações por nós estabelecidas, \
como a qualidade da água, a disponibilidade de comida e a presença de pescadores."

def portrayal_method(agent):
    portrayal = {"Filled": "true", "Layer": 0, "w": 1, "h": 1}
    if type(agent) is ShoalAgent:
        if not agent.eated:
            portrayal["Shape"] = "assets/cardume.png"
    elif type(agent) is PinkDolphinAgent:
        portrayal["Shape"] = "assets/pink_dolphin.jpg"
    elif type(agent) is WaterAgent:
        portrayal["Shape"] = "assets/water.png"
    return portrayal


grid = CanvasGrid(portrayal_method, 15, 15, 550, 550)
server = ModularServer(
    Model, [grid], "Pink Dolphin", {"num_agents": 25, "width": 15, "height": 15}
)
server.description = descricao
server.port = 8001
server.launch()
