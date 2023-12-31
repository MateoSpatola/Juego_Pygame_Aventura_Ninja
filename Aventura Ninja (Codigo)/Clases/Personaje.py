import pygame
from Clases.Objeto_Juego import *
from Clases.Proyectil import Proyectil
from Clases.Niveles.Nivel_Uno import *
from Clases.configuraciones import *


class Personaje(Objeto_Juego):
    def __init__(self, animaciones:dict, que_animacion:str, posicion_inicial:tuple, velocidad):
        super().__init__(animaciones, que_animacion, posicion_inicial)

        #MOVIMIENTO
        self.desplazamiento_x = 0  #En el eje x
        self.desplazamiento_y = 0  #En el eje y
        
        #GRAVEDAD
        self.velocidad = velocidad
        self.gravedad = 0.8
        self.potencia_salto = -17

        self.esta_en_el_aire = True
        if self.que_animacion == "quieto_derecha":
            self.mira_derecha = True
        elif self.que_animacion == "quieto_izquierda":
            self.mira_derecha = False
        self.colisionando = False

        self.vidas_restantes = 3
        self.kunais_restantes = 100
        self.contador_pasos = 0
        self.contador_lanzar = 0
        self.recibio_daño = False
        self.lanzo = False

        self.lista_proyectiles = []
        self.sonido_proyectil = pygame.mixer.Sound("Recursos\Sonidos\proyectil.wav")
        self.sonido_proyectil.set_volume(1)

        self.sonido_golpe_espada = pygame.mixer.Sound("Recursos\Sonidos\golpe_espada.wav")
        self.sonido_golpe_espada.set_volume(1)

        self.sonido_personaje_dolor = pygame.mixer.Sound("Recursos\Sonidos\personaje_dolor.wav")
        self.sonido_personaje_dolor.set_volume(1)

    def mover(self):
        for lado in self.lados:
            self.lados[lado].x += self.desplazamiento_x * self.velocidad
    
    def saltar(self):
        self.desplazamiento_y = self.potencia_salto
        self.esta_en_el_aire = True
    
    def restar_vida_controlado(self):
        if self.recibio_daño == False:
            self.vidas_restantes -= 1
            self.sonido_personaje_dolor.play()
            self.recibio_daño = True
        elif self.contador_pasos > 5:
            self.contador_pasos = 0
            self.recibio_daño = False
        else:
            self.contador_pasos += 1

    def aplicar_gravedad(self, pantalla):
        self.salta(pantalla)
        self.desplazamiento_y += self.gravedad
        self.esta_en_el_aire = True
        for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
    
    def verificar_colision_plataformas_horizontal(self, lista_plataformas:list):
        self.mover() 
        self.colisionando = False
        for plataforma in lista_plataformas:
            if self.lados["main"].colliderect(plataforma.lados["main"]):
                self.colisionando = True
                if self.desplazamiento_x < 0: #Va a la izquierda
                    self.lados["main"].left = plataforma.lados["main"].right
                    self.lados = self.obtener_rectangulos(self.lados["main"])
                elif self.desplazamiento_x > 0: #Va a la derecha
                    self.lados["main"].right = plataforma.lados["main"].left
                    self.lados = self.obtener_rectangulos(self.lados["main"])

    def verificar_colision_plataformas_vertical(self, pantalla, lista_plataformas:list):
        self.aplicar_gravedad(pantalla)
        for plataforma in lista_plataformas:
            if self.lados["main"].colliderect(plataforma.lados["main"]):
                if self.desplazamiento_y > 0: #Baja
                    self.lados["main"].bottom = plataforma.lados["main"].top
                    self.lados = self.obtener_rectangulos(self.lados["main"])
                    self.desplazamiento_y = 0
                    self.esta_en_el_aire = False
                elif self.desplazamiento_y < 0: #Sube
                    self.lados["main"].top = plataforma.lados["main"].bottom
                    self.lados = self.obtener_rectangulos(self.lados["main"])
                    self.desplazamiento_y = 0

    def modificar_rectangulo(self, animacion:str):
        nuevo_rectangulo = self.animaciones[animacion][0].get_rect()
        nuevo_rectangulo.x = self.rectangulo.x
        nuevo_rectangulo.y = self.rectangulo.y
        self.rectangulo = nuevo_rectangulo
        self.lados = self.obtener_rectangulos(self.rectangulo)

    def lanzar_proyectil(self):
        if self.mira_derecha:
            posicion_x = self.lados["right"].x + 10
            velocidad = 8
            animacion = "proyectil_ninja_derecha"
        else:
            posicion_x = self.lados["left"].x - 40
            velocidad = -8
            animacion = "proyectil_ninja_izquierda"
        posicion_y = self.lados["bottom"].y - 31
        proyectil = Proyectil(diccionario_proyectiles, animacion, (posicion_x, posicion_y), velocidad)
        self.lista_proyectiles.append(proyectil)


    def camina_derecha(self, pantalla):
        if self.esta_en_el_aire == False:
            self.modificar_rectangulo("camina_derecha")
            #self.lados["main"] = pygame.Rect(self.lados["main"].left-25, self.lados["main"].top-55, self.lados["main"].width, self.lados["main"].height)
            #self.lados = self.obtener_rectangulos(self.lados["main"])
            self.blitear_animacion(pantalla, "camina_derecha")
    def camina_izquierda(self, pantalla):
        if self.esta_en_el_aire == False:
            self.modificar_rectangulo("camina_izquierda")
            #self.lados["main"] = pygame.Rect(self.lados["main"].left-22, self.lados["main"].top, self.lados["main"].width, self.lados["main"].height)
            #self.lados = self.obtener_rectangulos(self.lados["main"])
            self.blitear_animacion(pantalla, "camina_izquierda")
        
    def quieto(self, pantalla):
        if self.esta_en_el_aire == False:
            if self.mira_derecha:
                direccion = "quieto_derecha"
            else:
                direccion = "quieto_izquierda"
            self.modificar_rectangulo(direccion)
            self.blitear_animacion(pantalla, direccion)

    def salta(self, pantalla):
        if self.esta_en_el_aire:
            if self.mira_derecha:
                direccion = "salta_derecha"
                #rectangulo = "quieto_derecha"
            else:
                direccion = "salta_izquierda"
                #rectangulo = "quieto_izquierda"
            self.modificar_rectangulo(direccion) #rectangulo (para que cuando salte tenga el rectangulo de quieto y eliminar el bug de que queda trabado)
            self.blitear_animacion(pantalla, direccion)
    
    def lanza(self, pantalla):
        if self.esta_en_el_aire == False:
            if self.mira_derecha:
                direccion = "lanza_derecha"
                ajuste_main_left = 17
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
                ajuste_main_left = 0
            else:
                direccion = "ataca_izquierda"
                ajuste_main_left = 61
            self.modificar_rectangulo(direccion)
            self.lados["main"] = pygame.Rect(self.lados["main"].left-ajuste_main_left, self.lados["main"].top, self.lados["main"].width, self.lados["main"].height-12) #height-12
            self.lados = self.obtener_rectangulos(self.lados["main"])
            self.blitear_animacion(pantalla, direccion)
    

    def blitear_animaciones(self, pantalla):
        match self.que_animacion:
            case "camina_derecha":
                self.camina_derecha(pantalla)
            case "camina_izquierda":
                self.camina_izquierda(pantalla)
            case "quieto":
                self.quieto(pantalla)
            case "salta":
                self.salta(pantalla)
            case "lanza":
                self.lanza(pantalla)
                if self.lanzo == False:
                    self.lanzar_proyectil()
                    self.sonido_proyectil.play()
                    self.kunais_restantes -=1
                    self.lanzo = True
                elif self.contador_lanzar < 5:
                    self.contador_lanzar += 1
                else:
                    self.contador_lanzar = 0
                    self.lanzo = False
                    
            case "ataca":
                self.ataca(pantalla)
                self.sonido_golpe_espada.play()
    
    def actualizar(self, pantalla, lista_plataformas:list):
        self.verificar_colision_plataformas_horizontal(lista_plataformas)
        self.verificar_colision_plataformas_vertical(pantalla, lista_plataformas)
        self.blitear_animaciones(pantalla)







