import pygame
from pygame.locals import *

from Clases.Formularios.API_Forms.GUI_label import *
from Clases.Formularios.API_Forms.GUI_slider import *
from Clases.Formularios.API_Forms.GUI_form import *
from Clases.Formularios.API_Forms.GUI_button_image import *
from Clases.Formularios.API_Forms.GUI_checkbox import *

class FormAjustes(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)

        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen

        self.flag_musica = True
        self.flag_sonidos = True

        self.label_titulo = Label(self._slave, 130, 0, 420, 100, "AJUSTES", "Comic Sans", 30, "Black", "Recursos\Formularios\casilla_2.png")
        self._btn_musica = CheckBox(screen=self._slave, x = 95, y = 120, master_x = x, master_y = y, w = 100, h = 100,
                                    path_image_on= "Recursos\Formularios\Botones\musica_2.png", path_image_off= "Recursos\Formularios\Botones\musica_1.png")
        self.slider_volumen_musica = Slider(self._slave, x, y, 210, 160, 250, 15, self.volumen_musica, "Green", "White")
        self.label_volumen_musica = Label(self._slave, 480, 143, 100, 50, "10%", "Comic Sans", 15, "Black", "Recursos\Formularios\casilla_1.png")
        self._btn_sonidos = CheckBox(screen=self._slave, x = 95, y = 250, master_x = x, master_y = y, w = 100, h = 100,
                                        path_image_on= "Recursos\Formularios\Botones\sonidos_2.png", path_image_off= "Recursos\Formularios\Botones\sonidos_1.png")
        self.slider_volumen_sonidos = Slider(self._slave, x, y, 210, 290, 250, 15, self.volumen_sonidos, "Green", "White")
        self.label_volumen_sonidos = Label(self._slave, 480, 273, 100, 50, "10%", "Comic Sans", 15, "Black", "Recursos\Formularios\casilla_1.png")
        self._btn_salir = Button_Image(screen=self._slave, x = 290, y = 400, master_x = x, master_y = y, w = 100, h = 100,
                                    onclick = self.btn_salir_click, onclick_param = "home", path_image = "Recursos\Formularios\Botones\salir.png")
        
        self.lista_widgets.append(self.label_titulo)
        self.lista_widgets.append(self._btn_musica)
        self.lista_widgets.append(self.slider_volumen_musica)
        self.lista_widgets.append(self.label_volumen_musica)
        self.lista_widgets.append(self._btn_sonidos)
        self.lista_widgets.append(self.slider_volumen_sonidos)
        self.lista_widgets.append(self.label_volumen_sonidos)
        self.lista_widgets.append(self._btn_salir)

    def btn_musica_click(self):
        if self._btn_musica.get_esta_prendido():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.flag_musica = not self.flag_musica

    def update_volumen_musica(self, lista_eventos):
        self.label_volumen_musica.set_text(f"{round(self.volumen_musica * 100)}%")
        self.volumen_musica = self.slider_volumen_musica.value
        pygame.mixer.music.set_volume(self.volumen_musica)

    def update_volumen_sonidos(self, lista_eventos):
        self.label_volumen_sonidos.set_text(f"{round(self.volumen_sonidos * 100)}%")
        self.volumen_sonidos = self.slider_volumen_sonidos.value

    def btn_salir_click(self, param):
        self.guardar_configuracion_audio()
        self.end_dialog()

    def update(self, lista_eventos):
        if self.active:
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.update_volumen_musica(lista_eventos)
            self.update_volumen_sonidos(lista_eventos)
            self.btn_musica_click()
            self.draw()


    