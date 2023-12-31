import pygame
from Clases.Item import *

class Recompensa(Item):
    def __init__(self, animaciones:dict, que_animacion:str, posicion_inicial:tuple):
        super().__init__(animaciones, que_animacion, posicion_inicial)

        self.sonido_moneda = pygame.mixer.Sound("Recursos\Sonidos\moneda.wav")
        self.sonido_moneda.set_volume(1)

        self.sonido_corazon = pygame.mixer.Sound("Recursos\Sonidos/corazon.wav")
        self.sonido_corazon.set_volume(1)

        self.sonido_kunai = pygame.mixer.Sound("Recursos\Sonidos\kunai.wav")
        self.sonido_kunai.set_volume(1)

    def aplicar_efecto(self, personaje_principal):
        if self.que_animacion == "moneda":
            self.sonido_moneda.play()
            personaje_principal.monedas_recolectadas += 1
        elif self.que_animacion == "corazon":
            self.sonido_corazon.play()
            personaje_principal.vidas_restantes += 1
        elif self.que_animacion == "kunai":
            self.sonido_kunai.play()
            personaje_principal.kunais_restantes += 1

