import pygame
from pygame.locals import *

from Clases.Formularios.API_Forms.GUI_button import *
from Clases.Formularios.API_Forms.GUI_slider import *
from Clases.Formularios.API_Forms.GUI_textbox import *
from Clases.Formularios.API_Forms.GUI_label import *
from Clases.Formularios.API_Forms.GUI_form import *
from Clases.Formularios.API_Forms.GUI_button_image import *
from Clases.Formularios.API_Forms.GUI_checkbox import *
from Clases.Formularios.API_Forms.GUI_picture_box import *
from Clases.Formularios.GUI.GUI_form_ajustes import *
from Clases.Formularios.GUI.GUI_form_seleccion_nivel import *
from Clases.Formularios.GUI.GUI_form_menu_ranking import *


class FormMenuPrincipal(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)

        self.fondo = pygame.image.load("Recursos/Ambientacion/fondo principal.jpg")
        self.fondo = pygame.transform.scale(self.fondo, (screen.get_width(), screen.get_height()))

        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen
        self.screen = screen

        self.btn_ajustes = Button_Image(self._slave, x, y, 150, 400, 100, 100, "Recursos\Formularios\Botones/ajustes.png", self.btn_ajustes_click, "Ajustes")
        self.btn_jugar = Button_Image(self._slave, x, y, 265, 380, 150, 150, "Recursos\Formularios\Botones\jugar.png", self.btn_jugar_click, "Jugar")
        self.btn_ranking = Button_Image(self._slave, x, y, 430, 400, 100, 100, "Recursos\Formularios\Botones/ranking.png", self.btn_ranking_click, "Ranking")
        self.label_titulo = Label(self._slave, 130, 0, 420, 100, "MENU PRINCIPAL", "Comic Sans", 30, "Black", "Recursos\Formularios\casilla_2.png")
        self.label_instrucciones = Label(self._slave, 100, 120, 480, 220, "Tecla F -> Lanzar | Tecla G -> Atacar", "Comic Sans", 20, "White", "Recursos\Formularios\casilla_3.png")

        self.lista_widgets.append(self.btn_ajustes)
        self.lista_widgets.append(self.btn_jugar)
        self.lista_widgets.append(self.btn_ranking)
        self.lista_widgets.append(self.label_titulo)
        self.lista_widgets.append(self.label_instrucciones)

        pygame.mixer.init()
        pygame.mixer.music.load("Recursos\Sonidos\musica_fondo.wav")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            self.screen.blit(self.fondo, (0,0))
            if self.active:
                self.draw()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)


    def btn_ajustes_click(self, param):
        form_ajustes = FormAjustes(self._master,
                                        300,
                                        50,
                                        680,
                                        620,
                                        True,
                                        "Recursos\Formularios\interfaz.png")
        self.show_dialog(form_ajustes)

    def btn_jugar_click(self, param):
        form_seleccion_nivel = FormSeleccionNivel(self._master,
                                        300,
                                        50,
                                        680,
                                        620,
                                        True,
                                        "Recursos\Formularios\interfaz.png")
        self.show_dialog(form_seleccion_nivel) #Este metodo se encarga de mostrar el formulario

    def btn_ranking_click(self, texto):
        lista_puntajes = self.obtener_top_tres_jugadores_db()
        
        form_ranking = FormMenuRanking(self._master,
                                        300,
                                        50,
                                        680,
                                        620,
                                        True,
                                        "Recursos\Formularios\interfaz.png",
                                        lista_puntajes,
                                        240,
                                        70,
                                        5
                                        )
        self.show_dialog(form_ranking)

    def obtener_top_tres_jugadores_db(self):
        with sqlite3.connect("Recursos\datos_jugadores.db") as conexion:
            try:
                lista_puntajes = []
                cursor = conexion.execute("select * from Puntuaciones order by puntaje desc limit 3")
                for fila in cursor:
                    dic = {}
                    dic["Nivel"] = fila[1]
                    dic["Jugador"] = fila[2]
                    dic["Puntaje"] = fila[3]
                    lista_puntajes.append(dic)
                print("Datos seleccionados con exito")
                return lista_puntajes
            except:
                print("Hubo un error al intentar seleccionar los datos de la base de datos :(")

