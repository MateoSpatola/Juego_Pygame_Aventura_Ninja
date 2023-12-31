import pygame, sys
from Clases.debug_mode import *
from Clases.configuraciones import *
from Clases.Personaje_Enemigo import Personaje_Enemigo
from Clases.Personaje_Boss_Samurai_Mek import Personaje_Boss_Samurai_Mek
from Clases.Plataforma import Plataforma
from Clases.Recompensa import Recompensa
from Clases.Trampa import Trampa


class Nivel():
    def __init__(self, pantalla, personaje_principal, imagen_fondo):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.img_fondo = imagen_fondo
        self.tiempo_restante = 60
        self.puntuacion = 0

        self.timer_event = pygame.USEREVENT + 0
        pygame.time.set_timer(self.timer_event, 1000)

        self.sonido_enemigo_muere = pygame.mixer.Sound("Recursos\Sonidos\enemigo_muere.wav")
        self.sonido_enemigo_muere.set_volume(1)

    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if evento.type == self.timer_event:
                self.tiempo_restante -= 1
        self.actualizar_pantalla()
        self.modo_programador()
        self.dibujar_grilla()
        self.blitear_barra_superior()
        self.calcular_puntuacion()

    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo, (0,0))
        for plataforma in self.plataformas:
            plataforma.actualizar(self._slave)
        for enemigo in self.enemigos:
            enemigo.actualizar(self._slave, self.plataformas)
            if enemigo.vidas_restantes == 0:
                    self.enemigos.remove(enemigo)
                    self.sonido_enemigo_muere.play()
                    self.jugador.asesinatos += 1
        for item in self.items:
            item.actualizar(self._slave)
        self.jugador.actualizar(self._slave, self.plataformas, self.enemigos, self.items)
        self.verificar_colisiones_proyectiles()

    def verificar_colisiones_proyectiles(self):
        for proyectil in self.jugador.lista_proyectiles:
                proyectil.actualizar(self._slave, self.jugador, self.enemigos, self.plataformas)
        for enemigo in self.enemigos:
            for proyectil in enemigo.lista_proyectiles:
                proyectil.actualizar(self._slave, enemigo, self.jugador, self.plataformas)

    def calcular_puntuacion(self):
        self.puntuacion = self.jugador.monedas_recolectadas * 50 + self.jugador.asesinatos * 100

    def blitear_barra_superior(self):
        pygame.draw.rect(self._slave, "Black", (420, 0, 440, 40), border_radius = 5)

        fuente = pygame.font.SysFont("Arial", 30)
        
        vidas = fuente.render(f": {self.jugador.vidas_restantes}", True, "White")
        self._slave.blit(recompensa_corazon[0],(430,-8))
        self._slave.blit(vidas,(455,2))

        kunais = fuente.render(f": {self.jugador.kunais_restantes}", True, "White")
        self._slave.blit(proyectil_ninja_derecha[0],(510,16))
        self._slave.blit(kunais,(550,2))

        tiempo = fuente.render(f"{self.tiempo_restante}", True, "Red")
        self._slave.blit(tiempo,(630,2))

        puntuacion = fuente.render(f"Puntaje: {self.puntuacion}", True, "White")
        self._slave.blit(puntuacion,(705,2))

    def modo_programador(self):
        #MODO PROGRAMADOR
        if get_mode():
            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, "Gray", self.jugador.lados[lado], 2)
                for proyectil in self.jugador.lista_proyectiles:
                    for lado in proyectil.lados:
                        pygame.draw.rect(self._slave, "Gray", proyectil.lados[lado], 2)

            for plataforma in self.plataformas:
                for lado in plataforma.lados:
                    pygame.draw.rect(self._slave, "Blue", plataforma.lados[lado], 2)
            
            for item in self.items:
                for lado in item.lados:
                    if isinstance(item, Recompensa):
                        pygame.draw.rect(self._slave, "Green", item.lados[lado], 2)
                    if isinstance(item, Trampa):
                        pygame.draw.rect(self._slave, "Orange", item.lados[lado], 2)

            for enemigo in self.enemigos:
                for lado in enemigo.lados:
                    pygame.draw.rect(self._slave, "Red", enemigo.lados[lado], 2)
                for proyectil in enemigo.lista_proyectiles:
                    for lado in proyectil.lados:
                        pygame.draw.rect(self._slave, "Red", proyectil.lados[lado], 2)

    def dibujar_grilla(self):
        if get_mode():
            tamaño = 40
            for line in range(0, 32):
                pygame.draw.line(self._slave, "White", (0, line * tamaño), (self._slave.get_width(), line * tamaño))
                pygame.draw.line(self._slave, "White", (line * tamaño, 0), (line * tamaño, self._slave.get_height()))


    '''POSICIONES OBJETOS ESCENARIO:
        0 -> Vacio
        1 -> Plataforma Piedra
        2 -> Plataforma Pasto
        3 -> Recompensa Moneda
        4 -> Recompensa Corazon
        5 -> Recompensa Kunai
        6 -> Trampa Pinchos
        7 -> Enemigo (Camina y Ataca)
        8 -> Enemigo (Quieto(der) y Lanza)
        9 -> Enemigo (Quieto(izq) y Lanza)
        10 -> BOSS (Camina, Salta, Lanza y Ataca)
        '''
    def blitear_escenario(self, escenario):
        self.plataformas = [] #lista_plataformas
        self.enemigos = [] #lista_enemigos
        self.items = [] #lista_items
        tamaño = 40
        contador_filas = 0
        for fila in escenario:
            contador_columnas = 0
            for cuadro in fila:
                if cuadro == 1:
                    self.plataformas.append(Plataforma(diccionario_plataformas, "piedra",
                                                       (contador_columnas * tamaño, contador_filas * tamaño)))
                if cuadro == 2:
                    self.plataformas.append(Plataforma(diccionario_plataformas, "pasto",
                                                       (contador_columnas * tamaño, contador_filas * tamaño)))
                if cuadro == 3:
                    self.items.append(Recompensa(diccionario_recompensas, "moneda",
                                                 (contador_columnas * tamaño + 10, contador_filas * tamaño + 10)))
                if cuadro == 4:
                    self.items.append(Recompensa(diccionario_recompensas, "corazon",
                                                 (contador_columnas * tamaño + 8, contador_filas * tamaño)))
                if cuadro == 5:
                    self.items.append(Recompensa(diccionario_recompensas, "kunai",
                                                 (contador_columnas * tamaño + 14, contador_filas * tamaño)))
                if cuadro == 6:
                    self.items.append(Trampa(diccionario_trampas, "pinchos",
                                             (contador_columnas * tamaño + 10, contador_filas * tamaño - 10)))
                if cuadro == 7:
                    self.enemigos.append(Personaje_Enemigo(diccionario_animaciones_ninja_enemigo_mujer, "quieto_derecha",
                                                           (contador_columnas * tamaño, contador_filas * tamaño), 4, True, False, False, True))
                if cuadro == 8:
                    self.enemigos.append(Personaje_Enemigo(diccionario_animaciones_ninja_enemigo_mujer, "quieto_derecha",
                                                           (contador_columnas * tamaño, contador_filas * tamaño), 4, False, False, True, False))
                if cuadro == 9:
                    self.enemigos.append(Personaje_Enemigo(diccionario_animaciones_ninja_enemigo_mujer, "quieto_izquierda",
                                                           (contador_columnas * tamaño, contador_filas * tamaño), 4, False, False, True, False))
                if cuadro == 10:
                    self.enemigos.append(Personaje_Boss_Samurai_Mek(diccionario_animaciones_boss_samurai_mek, "quieto_derecha",
                                                                    (contador_columnas * tamaño, contador_filas * tamaño), 5, True, True, True, True))
                contador_columnas += 1
            contador_filas += 1