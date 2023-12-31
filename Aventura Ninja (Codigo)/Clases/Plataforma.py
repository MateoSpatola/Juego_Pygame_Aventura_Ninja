import pygame
from Clases.Objeto_Juego import *

class Plataforma(Objeto_Juego):
    def __init__(self, animaciones:dict, que_animacion:str, posicion_inicial:tuple):
        super().__init__(animaciones, que_animacion, posicion_inicial)

