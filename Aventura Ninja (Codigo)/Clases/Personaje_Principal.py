import pygame
from Clases.Personaje import *
#from Clases.Item import Item
from Clases.Recompensa import Recompensa
from Clases.Trampa import Trampa

class Personaje_Principal(Personaje):
    def __init__(self, animaciones:dict, que_animacion:str, posicion_inicial:tuple, velocidad):
        super().__init__(animaciones, que_animacion, posicion_inicial, velocidad)
        self.monedas_recolectadas = 0
        self.vidas_restantes = 3
        self.kunais_restantes = 3
        self.asesinatos = 0

    def verificar_eventos_personaje(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.que_animacion = "camina_derecha"
            self.desplazamiento_x = 1
            self.mira_derecha = True
        elif keys[pygame.K_LEFT]:
            self.que_animacion = "camina_izquierda"
            self.desplazamiento_x = -1
            self.mira_derecha = False
        else:
            self.que_animacion = "quieto"
            self.desplazamiento_x = 0
        
        if keys[pygame.K_SPACE]:
            if self.esta_en_el_aire == False:
                self.que_animacion = "salta"
                self.saltar()
        if keys[pygame.K_f]:
            if self.kunais_restantes > 0:
                self.que_animacion = "lanza"
        if keys[pygame.K_g]:
            self.que_animacion = "ataca"

    def verificar_colision_items(self, lista_items):
        for item in lista_items:
            if self.lados["main"].colliderect(item.lados["main"]):
                item.aplicar_efecto(self)
                if isinstance(item, Recompensa): #Si el item es una instancia de la clase recompensa lo elimino de la lista
                    lista_items.remove(item)
        return lista_items

    def atacar_enemigos(self, lista_enemigos):
        if self.que_animacion == "ataca":
            for enemigo in lista_enemigos:
                if self.mira_derecha:
                    if self.lados["right"].colliderect(enemigo.lados["main"]):
                        enemigo.desplazamiento_y = -7
                        enemigo.restar_vida_controlado()
                else:
                    if self.lados["left"].colliderect(enemigo.lados["main"]):
                        enemigo.desplazamiento_y = -7
                        enemigo.restar_vida_controlado()

    def recibir_daño(self, lista_enemigos):
        for enemigo in lista_enemigos:
            if enemigo.que_animacion == "ataca":
                if enemigo.mira_derecha:
                    if enemigo.lados["right"].colliderect(self.lados["main"]):
                        self.desplazamiento_y = -7
                        self.restar_vida_controlado()
                else:
                    if enemigo.lados["left"].colliderect(self.lados["main"]):
                        self.desplazamiento_y = -7
                        self.restar_vida_controlado()
                        
    def actualizar(self, pantalla, lista_plataformas:list, lista_enemigos:list, lista_items:list):
        self.verificar_eventos_personaje()
        self.atacar_enemigos(lista_enemigos)
        self.verificar_colision_items(lista_items)
        self.recibir_daño(lista_enemigos)
        return super().actualizar(pantalla, lista_plataformas)