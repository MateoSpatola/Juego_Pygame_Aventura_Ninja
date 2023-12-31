import pygame
from pygame.locals import *

from Clases.Formularios.API_Forms.GUI_label import *
from Clases.Formularios.API_Forms.GUI_form import *
from Clases.Formularios.API_Forms.GUI_button_image import *

class FormMenuRanking(Form):
    def __init__(self, screen, x, y, w, h, active, path_image, lista_puntajes, margen_y, margen_x, espacio):
        super().__init__(screen, x, y, w, h, active)

        self.fondo = pygame.image.load("Recursos/Ambientacion/fondo principal.jpg")
        self.fondo = pygame.transform.scale(self.fondo, (screen.get_width(), screen.get_height()))

        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))

        self._slave = aux_imagen
        self.screen = screen
        self._lista_puntajes = lista_puntajes

        self.margen_y = margen_y

        self.label_titulo = Label(self._slave, 130, 0, 420, 100, "RANKING", "Comic Sans", 30, "Black", "Recursos\Formularios\casilla_2.png")

        lbl_nivel = Label(self._slave, x= 70, y= 140, w= 170, h= 80, text= "NIVEL",
                        font= "Comic Sans", font_size= 25, font_color= "White", path_image= "Recursos\Formularios\casilla_3.png")
        
        lbl_jugador = Label(self._slave, x= 255, y= 140, w= 170, h= 80, text= "JUGADOR",
                        font= "Comic Sans", font_size= 25, font_color= "White", path_image= "Recursos\Formularios\casilla_3.png")
        
        lbl_puntaje = Label(self._slave, x= 440, y= 140, w= 170, h= 80, text= "PUNTAJE",
                        font= "Comic Sans", font_size= 25, font_color= "White", path_image= "Recursos\Formularios\casilla_3.png")
        
        
        self.lista_widgets.append(self.label_titulo)
        self.lista_widgets.append(lbl_nivel)
        self.lista_widgets.append(lbl_jugador)
        self.lista_widgets.append(lbl_puntaje)

        try:
            pos_inicial_y = margen_y
            for j in self._lista_puntajes:
                pos_inicial_x = margen_x
                for n,s in j.items():
                    cadena = ""
                    cadena = f"{s}"
                    item = Label(self._slave, pos_inicial_x, pos_inicial_y, 170, 50, cadena, "Comic Sans", 20,
                                    "White", "Recursos\Formularios\casilla_3.png")
                    self.lista_widgets.append(item)
                    pos_inicial_x += 185
                pos_inicial_y += 50 + espacio
        except:
            self.label_no_hay_datos = Label(self._slave, 100, 250, 480, 120, "No hay datos para mostrar", "Comic Sans", 20, "White", "Recursos\Formularios\casilla_3.png")
            self.lista_widgets.append(self.label_no_hay_datos)


        self._btn_home = Button_Image(screen=self._slave,
                                        x = 290,
                                        y = 430,
                                        master_x = x,
                                        master_y = y,
                                        w = 100,
                                        h = 100,
                                        onclick = self.btn_home_click,
                                        onclick_param = "home",
                                        path_image = "Recursos\Formularios\Botones\home.png")
        
        self.lista_widgets.append(self._btn_home)

    def btn_home_click(self, param):
        self.end_dialog()


    def update(self, lista_eventos):
        if self.active:
            self.screen.blit(self.fondo, (0,0))
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()