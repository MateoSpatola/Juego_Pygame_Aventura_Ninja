import pygame
from Clases.Personaje import *
import random

class Personaje_Enemigo(Personaje):
    def __init__(self, animaciones:dict, que_animacion:str, posicion_inicial:tuple, velocidad, puede_moverse:bool, puede_saltar:bool, puede_lanzar:bool, puede_atacar:bool):
        super().__init__(animaciones, que_animacion, posicion_inicial, velocidad)

        self.desplazamiento_x = 0
        self.comportamiento = 0
        self.contador_comportamiento = 0
        self.tiene_direccion = False
        self.vidas_restantes = 2
        self.puede_moverse = puede_moverse
        self.puede_saltar = puede_saltar
        self.puede_lanzar = puede_lanzar
        self.puede_atacar = puede_atacar

    def generar_direccion_aleatoria(self):
        if self.tiene_direccion == False:
            self.desplazamiento_x = random.choice([-1, 1])
            self.tiene_direccion = True
    
    def generar_comportamiento_aleatorio_cada_cierto_tiempo(self, segundos):
        tiempo = segundos * 30
        self.contador_comportamiento += 1
        if self.contador_comportamiento > tiempo:
            self.comportamiento = random.choice([1,2,3])
            self.contador_comportamiento = 0

    def realizar_comportamiento(self, lista_plataformas: list):
        if self.desplazamiento_x == 1:
            self.que_animacion = "camina_derecha"
            self.mira_derecha = True
            if self.colisionando == True:
                self.desplazamiento_x = -1
                self.colisionando = False
            self.generar_comportamiento_aleatorio_cada_cierto_tiempo(2)

        elif self.desplazamiento_x == -1:
            self.que_animacion = "camina_izquierda"
            self.mira_derecha = False
            if self.colisionando == True:
                self.desplazamiento_x = 1
                self.colisionando = False
            self.generar_comportamiento_aleatorio_cada_cierto_tiempo(2)

        else:
            self.que_animacion = "quieto"
            self.contador_comportamiento += 1
            if self.puede_moverse == True:
                if self.contador_comportamiento > 60:
                    self.contador_comportamiento = 0
                    self.generar_direccion_aleatoria()
            self.generar_comportamiento_aleatorio_cada_cierto_tiempo(2)

        if self.comportamiento == 1:
            if self.puede_saltar == True:
                if self.esta_en_el_aire == False and self.colisionando == False:
                    self.que_animacion = "salta"
                    self.saltar()
                self.comportamiento = 0
            else:
                self.comportamiento = 0

        elif self.comportamiento == 2:
            if self.puede_lanzar == True:
                if self.esta_en_el_aire == False and self.colisionando == False:
                    self.que_animacion = "lanza"
                    if self.contador_comportamiento > 45:
                        self.contador_comportamiento = 0
                        self.comportamiento = 0
                    else:
                        self.contador_comportamiento += 1
            else:
                self.comportamiento = 0
            
        elif self.comportamiento == 3:
            if self.puede_atacar == True:
                if self.esta_en_el_aire == False and self.colisionando == False:
                    self.que_animacion = "ataca"
                    self.contador_comportamiento += 1
                    self.verificar_colision_plataformas_horizontal(lista_plataformas)
                    if self.contador_comportamiento > 60 or self.colisionando == True:
                        self.contador_comportamiento = 0
                        self.comportamiento = 0
            else:
                self.comportamiento = 0


    def actualizar(self, pantalla, lista_plataformas: list):
        self.realizar_comportamiento(lista_plataformas)
        return super().actualizar(pantalla, lista_plataformas)
