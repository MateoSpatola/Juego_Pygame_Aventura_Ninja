import pygame
from Clases.Item import *
from Clases.Proyectil import Proyectil

class Trampa(Item):
    def __init__(self, animaciones:dict, que_animacion:str, posicion_inicial:tuple):
        super().__init__(animaciones, que_animacion, posicion_inicial)
        self.sonido_personaje_dolor = pygame.mixer.Sound("Recursos\Sonidos\personaje_dolor.wav")
        self.sonido_personaje_dolor.set_volume(1)

    def aplicar_efecto(self, personaje_principal):
        personaje_principal.vidas_restantes -= 1
        personaje_principal.desplazamiento_y = -7
        self.sonido_personaje_dolor.play()

        

