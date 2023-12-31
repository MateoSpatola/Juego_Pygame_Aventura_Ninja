import pygame
from pygame.locals import *

from Clases.Formularios.API_Forms.GUI_label import *
from Clases.Formularios.API_Forms.GUI_form import *
from Clases.Formularios.API_Forms.GUI_button_image import *
from Clases.Formularios.GUI.GUI_form_ajustes import *

class FormPausa(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)

        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen

        self._btn_jugar = Button_Image(screen=self._slave,
                                        x = 265,
                                        y = 200,
                                        master_x = x,
                                        master_y = y,
                                        w = 150,
                                        h = 150,
                                        onclick = self.btn_jugar_click,
                                        onclick_param = "jugar",
                                        path_image = "Recursos\Formularios\Botones\jugar.png")
        
        self.btn_ajustes = Button_Image(self._slave, x, y, 290, 400, 100, 100, "Recursos\Formularios\Botones/ajustes.png", self.btn_ajustes_click, "Ajustes")
        
        self.label_titulo = Label(self._slave, 130, 0, 420, 100, "JUEGO PAUSADO", "Comic Sans", 30, "Black", "Recursos\Formularios\casilla_2.png")
        
        self.lista_widgets.append(self._btn_jugar)
        self.lista_widgets.append(self.btn_ajustes)
        self.lista_widgets.append(self.label_titulo)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def btn_jugar_click(self, param):
        self.end_dialog()

    def btn_ajustes_click(self, param):
        form_ajustes = FormAjustes(self._master,
                                        300,
                                        50,
                                        680,
                                        620,
                                        True,
                                        "Recursos\Formularios\interfaz.png")
        self.show_dialog(form_ajustes)