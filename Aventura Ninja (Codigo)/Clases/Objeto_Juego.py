import pygame
from Clases.configuraciones import *

class Objeto_Juego():
    def __init__(self, animaciones:list, que_animacion:str, posicion_inicial:tuple):
        #ANIMACIONES
        self.contador_animaciones = 0
        self.que_animacion = que_animacion
        self.animaciones = animaciones

        #RECTANGULOS
        self.rectangulo = self.animaciones[que_animacion][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = self.obtener_rectangulos(self.rectangulo)

    def blitear_animacion(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_animaciones >= largo:
            self.contador_animaciones = 0
        pantalla.blit(animacion[self.contador_animaciones], self.lados["main"])
        self.contador_animaciones += 1

    def obtener_rectangulos(self, principal)->dict:
        self.diccionario_rectangulos = {}
        self.diccionario_rectangulos["main"] = principal
        self.diccionario_rectangulos["bottom"] = pygame.Rect(principal.left, principal.bottom-10, principal.width, 10)
        self.diccionario_rectangulos["right"] = pygame.Rect(principal.right-10, principal.top, 10, principal.height)
        self.diccionario_rectangulos["left"] = pygame.Rect(principal.left, principal.top, 10, principal.height)
        self.diccionario_rectangulos["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
        return self.diccionario_rectangulos

    def actualizar(self, pantalla):
        self.blitear_animacion(pantalla, self.que_animacion)
                