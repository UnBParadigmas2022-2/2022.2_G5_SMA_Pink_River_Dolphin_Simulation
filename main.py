from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from src.ShoalAgent import ShoalAgent
from src.PinkDolphinAgent import PinkDolphinAgent
from src.WaterAgent import WaterAgent
from src.Poluente import Poluente
from src.Model import Model
from src.FisherAgent import FisherAgent
import mesa

descricao = "Seguindo a temática de animais em risco de extinção aplicada nas duas últimas entregas, \
decidimos desenvolver um sistema que simule as rotas migratórias do Boto Cor de Rosa, \
tendo como base determinadas complicações por nós estabelecidas, \
como a qualidade da água, a disponibilidade de comida e a presença de pescadores."

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
    
    elif type(agent) is FisherAgent:
        portrayal["Shape"] = "assets/fisher.png"

    elif type(agent) is WaterAgent:
        if agent.qualidade == 2:
            portrayal["Shape"] = "rect"
            portrayal["Color"] = "yellow"
        elif agent.qualidade == 1:
            portrayal["Shape"] = "rect"
            portrayal["Color"] = "green"
        else:
            portrayal["Shape"] = "rect"
            portrayal["Color"] = "blue"

    elif type(agent) is Poluente:
        portrayal["Shape"] = "assets/trash.png"

    return portrayal

model_params = {
    "num_dolphin": mesa.visualization.Slider(
        "População de Botos", 5, 1, 20
    ),
    "num_agents": mesa.visualization.Slider(
        "População Inicial de cardumes", 10, 30, 60
    ),
    "num_poluentes": mesa.visualization.Slider(
        "Quantidade de poluentes", 1, 1, 5
    ),
}

grid = CanvasGrid(portrayal_method, 25, 25, 600, 600)

server = ModularServer(
    Model, [grid], "Pink Dolphin", model_params
)
server.description = descricao
server.port = 8001
server.launch()
