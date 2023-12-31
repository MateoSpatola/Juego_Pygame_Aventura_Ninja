import pygame
from Clases.Personaje_Enemigo import *

class Personaje_Boss_Samurai_Mek(Personaje_Enemigo):
    def __init__(self, animaciones:dict, que_animacion:str, posicion_inicial:tuple, velocidad, puede_moverse:bool, puede_saltar:bool, puede_lanzar:bool, puede_atacar:bool):
        super().__init__(animaciones, que_animacion, posicion_inicial, velocidad, puede_moverse, puede_saltar, puede_lanzar, puede_atacar)
        self.vidas_restantes = 3


    def lanzar_proyectil(self):
        if self.mira_derecha:
            posicion_x = self.lados["right"].x + 10
            velocidad = 10
            animacion = "proyectil_Samurai_Mek_derecha"
        else:
            posicion_x = self.lados["left"].x - 40
            velocidad = -10
            animacion = "proyectil_Samurai_Mek_izquierda"
        posicion_y = self.lados["bottom"].y - 50
        proyectil = Proyectil(diccionario_proyectiles, animacion, (posicion_x, posicion_y), velocidad)
        self.lista_proyectiles.append(proyectil)
    
    def lanza(self, pantalla):
        if self.esta_en_el_aire == False:
            if self.mira_derecha:
                direccion = "lanza_derecha"
                ajuste_main_left = 6
            else:
                direccion = "lanza_izquierda"
                ajuste_main_left = 12
            self.modificar_rectangulo(direccion)
            self.lados["main"] = pygame.Rect(self.lados["main"].left-ajuste_main_left, self.lados["main"].top+1, self.lados["main"].width, self.lados["main"].height-1)
            self.lados = self.obtener_rectangulos(self.lados["main"])
            self.blitear_animacion(pantalla, direccion)

    def ataca(self, pantalla):
        if self.esta_en_el_aire == False:
            if self.mira_derecha:
                direccion = "ataca_derecha"
                ajuste_main_left = 16
            else:
                direccion = "ataca_izquierda"
                ajuste_main_left = 34
            self.modificar_rectangulo(direccion)
            self.lados["main"] = pygame.Rect(self.lados["main"].left-ajuste_main_left, self.lados["main"].top-8, self.lados["main"].width, self.lados["main"].height-8) #height-12
            self.lados = self.obtener_rectangulos(self.lados["main"])
            self.blitear_animacion(pantalla, direccion)

    def actualizar(self, pantalla, lista_plataformas:list):
        self.verificar_colision_plataformas_horizontal(lista_plataformas)
        self.verificar_colision_plataformas_vertical(pantalla, lista_plataformas)
        self.blitear_animaciones(pantalla)
        self.realizar_comportamiento(lista_plataformas)
