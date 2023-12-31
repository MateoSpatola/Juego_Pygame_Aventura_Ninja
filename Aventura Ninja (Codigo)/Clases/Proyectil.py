import pygame
from Clases.Item import *
from Clases.Nivel import *
from Clases.configuraciones import *

class Proyectil(Item):
    def __init__(self, animaciones:dict, que_animacion:str, posicion_inicial:tuple, velocidad):
        super().__init__(animaciones, que_animacion, posicion_inicial)
        self.velocidad = velocidad

        self.sonido_personaje_dolor = pygame.mixer.Sound("Recursos\Sonidos\personaje_dolor.wav")
        self.sonido_personaje_dolor.set_volume(1)

    def dar_trayectoria(self):
        for lado in self.lados:
            self.lados[lado].x += self.velocidad
        
    def aplicar_efecto(self, personaje):
        personaje.vidas_restantes -= 1
        personaje.desplazamiento_y = -7
        self.sonido_personaje_dolor.play()

    def verificar_objetivo(self, personaje_que_lanzo, personaje_donde_impacto, lista_plataformas):
        for plataforma in lista_plataformas:
            if plataforma.lados["main"].colliderect(self.lados["main"]):
                personaje_que_lanzo.lista_proyectiles.remove(self)
                return personaje_que_lanzo.lista_proyectiles
        if type(personaje_donde_impacto) != list:
            if personaje_donde_impacto.lados["main"].colliderect(self.lados["main"]):
                self.aplicar_efecto(personaje_donde_impacto)
                personaje_que_lanzo.lista_proyectiles.remove(self)
            return personaje_que_lanzo.lista_proyectiles
        else:
            for personaje in personaje_donde_impacto:
                if personaje.lados["main"].colliderect(self.lados["main"]):
                    self.aplicar_efecto(personaje)
                    try:
                        personaje_que_lanzo.lista_proyectiles.remove(self)
                    except:
                        print("Error al remover el proyectil")
            return personaje_que_lanzo.lista_proyectiles

    def actualizar(self, pantalla, personaje_que_lanzo, personaje_donde_impacto, lista_plataformas):
        self.dar_trayectoria()
        self.verificar_objetivo(personaje_que_lanzo, personaje_donde_impacto, lista_plataformas)
        return super().actualizar(pantalla)
        

