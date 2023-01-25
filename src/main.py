from server.settings import *
from server.config import Configuration

server = Configuration(
    GRID_WIDTH, 
    GRID_HEIGHT,
    CANVAS_WIDTH,
    CANVAS_HEIGHT,
    SERVER_PORT,
    NUMBER_OF_AGENTS)

server.configure_grid()
server.configure_server()
server.run_server()
