import pygame
from pygame.locals import *

from Clases.Formularios.API_Forms.GUI_label import *
from Clases.Formularios.API_Forms.GUI_form import *
from Clases.Formularios.API_Forms.GUI_button_image import *
from Clases.Formularios.GUI.GUI_form_contenedor_nivel import *
from Clases.Manejador_Niveles import Manejador_Niveles

class FormSeleccionNivel(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)

        self.fondo = pygame.image.load("Recursos/Ambientacion/fondo seleccion nivel.jpg")
        self.fondo = pygame.transform.scale(self.fondo, (screen.get_width(), screen.get_height()))

        self.manejador_niveles = Manejador_Niveles(self._master)
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self.screen = screen
        
        self._slave = aux_imagen
        self.aux_x = x
        self.aux_y = y
        self.botones_cargados = False

        self._btn_home = Button_Image(screen=self._slave,
                                        x = 290,
                                        y = 400,
                                        master_x = x,
                                        master_y = y,
                                        w = 100,
                                        h = 100,
                                        onclick = self.btn_home_click,
                                        onclick_param = "home",
                                        path_image = "Recursos\Formularios\Botones\home.png")
        
        self.label_titulo = Label(self._slave, 130, 0, 420, 100, "SELECCIONAR NIVEL", "Comic Sans", 30, "Black", "Recursos\Formularios\casilla_2.png")
        
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self.label_titulo)

    def cargar_botones(self):
        self._btn_nivel_1 = Button_Image(screen=self._slave,
                                        x = 95,
                                        y = 220,
                                        master_x = self.aux_x,
                                        master_y = self.aux_y,
                                        w = 150,
                                        h = 150,
                                        onclick = self.entrar_nivel,
                                        onclick_param = "nivel_uno",
                                        path_image = "Recursos\Formularios\Botones/1.png")

        if self.progreso == 1:
            path_image_nivel_2 = "Recursos\Formularios\Botones/bloqueado.png"
        else:
            path_image_nivel_2 = "Recursos\Formularios\Botones/2.png"
        self._btn_nivel_2 = Button_Image(screen=self._slave,
                                            x = 265,
                                            y = 220,
                                            master_x = self.aux_x,
                                            master_y = self.aux_y,
                                            w = 150,
                                            h = 150,
                                            onclick = self.entrar_nivel,
                                            onclick_param = "nivel_dos",
                                            path_image = path_image_nivel_2)
        
        if self.progreso <= 2:
            path_image_nivel_3 = "Recursos\Formularios\Botones/bloqueado.png"
        else:
            path_image_nivel_3 = "Recursos\Formularios\Botones/3.png"
        self._btn_nivel_3 = Button_Image(screen=self._slave,
                                        x = 435,
                                        y = 220,
                                        master_x = self.aux_x,
                                        master_y = self.aux_y,
                                        w = 150,
                                        h = 150,
                                        onclick = self.entrar_nivel,
                                        onclick_param = "nivel_tres",
                                        path_image = path_image_nivel_3)

        self.lista_widgets.append(self._btn_nivel_1)
        self.lista_widgets.append(self._btn_nivel_2)
        self.lista_widgets.append(self._btn_nivel_3)
        self.botones_cargados = True

    def update(self, lista_eventos):
        self.progreso = self.cargar_progreso()
        if self.verificar_dialog_result():
            if self.botones_cargados == False:
                self.cargar_botones()
            self.screen.blit(self.fondo, (0,0))
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
            self.botones_cargados = False
            
    def entrar_nivel(self, nombre_nivel):
        if nombre_nivel == "nivel_dos":
            if self.progreso >= 2:
                nivel = self.manejador_niveles.get_nivel(nombre_nivel)
                form_contenedor_nivel = FormContenedorNivel(self._master, nivel, nombre_nivel, self)
                self.show_dialog(form_contenedor_nivel)
            else:
                print("Primero complete el nivel 1")
        elif nombre_nivel == "nivel_tres":
            if self.progreso == 3:
                nivel = self.manejador_niveles.get_nivel(nombre_nivel)
                form_contenedor_nivel = FormContenedorNivel(self._master, nivel, nombre_nivel, self)
                self.show_dialog(form_contenedor_nivel)
            else:
                print("Primero complete el nivel 1 y 2")
        else:
            nivel = self.manejador_niveles.get_nivel(nombre_nivel)
            form_contenedor_nivel = FormContenedorNivel(self._master, nivel, nombre_nivel, self)
            self.show_dialog(form_contenedor_nivel)

    def btn_home_click(self, param):
        self.end_dialog()