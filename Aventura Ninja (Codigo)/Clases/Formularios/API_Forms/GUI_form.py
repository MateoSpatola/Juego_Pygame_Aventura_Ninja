import pygame, json
from pygame.locals import *

from Clases.Formularios.API_Forms.GUI_button import *
#No se instancia. Es la base de la jerarquia
class Form(Widget):
    def __init__(self, screen, x,y,w,h,color_background,color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x,y,w,h, color_background, color_border, border_size)
        self._slave = pygame.Surface((w,h))
        self.slave_rect = self._slave.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        self.lista_widgets = []
        self.hijo = None
        self.dialog_result = None
        self.padre = None

        self.volumen_musica, self.volumen_sonidos = self.cargar_configuracion_audio()
        self.progreso = self.cargar_progreso()
    
    def show_dialog(self, formulario):
        self.hijo = formulario
        self.hijo.padre = self

    def end_dialog(self):
        self.dialog_result = "OK"
        self.close()

    def close(self):
        self.active = False

    def verificar_dialog_result(self):
        return self.hijo == None or self.hijo.dialog_result != None
 
    def render(self):
        pass
    def update(self, lista_eventos):
        pass
    
    def cargar_configuracion_audio(self):
        try:
            with open("Recursos\configuracion_audio.txt", "r") as archivo:
                for linea in archivo.readlines():
                    if linea.startswith("musica"):
                        self.volumen_musica = float(linea.split(":")[1])
                    if linea.startswith("sonidos"):
                        self.volumen_sonidos = float(linea.split(":")[1])
        except FileNotFoundError:
            self.volumen_musica = 0.1
            self.volumen_sonidos = 0.5
        return self.volumen_musica, self.volumen_sonidos
    
    def guardar_configuracion_audio(self):
        with open("Recursos\configuracion_audio.txt", "w") as archivo:
            archivo.write("musica:{}\nsonidos:{}".format(self.volumen_musica, self.volumen_sonidos))

    def guardar_progreso(self, nivel_alcanzado):
        data = {"nivel":nivel_alcanzado}
        with open("Recursos\progreso.json", "w") as archivo:
            json.dump(data, archivo)

    def cargar_progreso(self):
        try:
            with open("Recursos\progreso.json", "r") as archivo:
                data = json.load(archivo)
                nivel = data["nivel"]
        except FileNotFoundError:
            nivel = 1
        return nivel