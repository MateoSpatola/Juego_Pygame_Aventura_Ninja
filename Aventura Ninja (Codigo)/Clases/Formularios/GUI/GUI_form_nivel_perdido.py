import pygame
from pygame.locals import *

from Clases.Formularios.API_Forms.GUI_label import *
from Clases.Formularios.API_Forms.GUI_form import *
from Clases.Formularios.API_Forms.GUI_button_image import *

class FormNivelPerdido(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)

        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen

        self._btn_reintentar = Button_Image(screen=self._slave,
                                        x = 265,
                                        y = 200,
                                        master_x = x,
                                        master_y = y,
                                        w = 150,
                                        h = 150,
                                        onclick = self.btn_reintentar_click,
                                        onclick_param = "jugar",
                                        path_image = "Recursos\Formularios\Botones/reintentar.png")
        
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
        
        self.label_titulo = Label(self._slave, 130, 0, 420, 100, "GAME OVER", "Comic Sans", 30, "Black", "Recursos\Formularios\casilla_2.png")
        
        self.lista_widgets.append(self._btn_reintentar)
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self.label_titulo)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def btn_home_click(self, param):
        self.end_dialog()

    def btn_reintentar_click(self, param):
        self.end_dialog()