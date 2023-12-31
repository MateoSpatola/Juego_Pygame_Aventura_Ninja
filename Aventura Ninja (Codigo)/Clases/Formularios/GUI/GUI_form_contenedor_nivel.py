import pygame
from pygame.locals import *

from Clases.Formularios.API_Forms.GUI_form import *
from Clases.Formularios.API_Forms.GUI_button_image import *
from Clases.Formularios.GUI.GUI_form_ajustes import *
from Clases.Formularios.GUI.GUI_form_nivel_perdido import *
from Clases.Formularios.GUI.GUI_form_nivel_completado import *
from Clases.Formularios.GUI.GUI_form_pausa import *
from Clases.Recompensa import *

class FormContenedorNivel(Form):
    def __init__(self, pantalla: pygame.Surface, nivel, nombre_nivel, form_seleccion_nivel):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(), color_background="Black")
        nivel._slave = self._slave
        self.nivel = nivel
        self.nombre_nivel = nombre_nivel
        self.form_seleccion_nivel = form_seleccion_nivel
        self.nivel_finalizado = False
        self._btn_home = Button_Image(screen=self._slave,
                                        master_x = self._x,
                                        master_y = self._y,
                                        x = self._w - 420,
                                        y = 0,
                                        w = 40,
                                        h = 40,
                                        onclick = self.btn_home_click,
                                        onclick_param = "home",
                                        path_image = "Recursos\Formularios\Botones\home.png")
        
        self._btn_pausa = Button_Image(screen=self._slave,
                                        master_x = self._x,
                                        master_y = self._y,
                                        x = self._w - 900,
                                        y = 0,
                                        w = 40,
                                        h = 40,
                                        onclick = self.btn_pausa_click,
                                        onclick_param = "pausa",
                                        path_image = "Recursos\Formularios\Botones\pausa.png")
        

        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self._btn_pausa)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            self.nivel.update(lista_eventos)
            self.update_sonidos(lista_eventos)
            self.finalizar_nivel()
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
    
    def btn_home_click(self, param):
        self.end_dialog()

    def btn_pausa_click(self, param):
        form_nivel_perdido = FormPausa(self._master,
                                                300,
                                                50,
                                                680,
                                                620,
                                                True,
                                                "Recursos\Formularios\interfaz.png")
        self.show_dialog(form_nivel_perdido)
        
            
    def finalizar_nivel(self):
        if len(self.nivel.enemigos) == 0 or self.nivel.tiempo_restante == 0:
            if self.nivel.puntuacion > 0:
                if self.nombre_nivel == "nivel_uno":
                    self.guardar_progreso(2)
                if self.nombre_nivel == "nivel_dos":
                    self.guardar_progreso(3)
                self.form_nivel_completado()
            else:
                self.form_nivel_perdido()
        elif self.nivel.jugador.vidas_restantes <= 0:
            self.form_nivel_perdido()
                
    def form_nivel_perdido(self):
        if self.nivel_finalizado:
                self.end_dialog()
        else:
            self.nivel_finalizado = True
            form_nivel_perdido = FormNivelPerdido(self._master,
                                            300,
                                            50,
                                            680,
                                            620,
                                            True,
                                            "Recursos\Formularios\interfaz.png")
            self.show_dialog(form_nivel_perdido)

    def form_nivel_completado(self):
        if self.nivel_finalizado:
            self.end_dialog()
        else:
            puntaje_final = self.nivel.puntuacion + self.nivel.tiempo_restante * 100
            self.nivel_finalizado = True
            form_nivel_completado = FormNivelCompletado(self._master,
                                            300,
                                            50,
                                            680,
                                            620,
                                            True,
                                            "Recursos\Formularios\interfaz.png",
                                            puntaje_final,
                                            self.nombre_nivel)
            self.show_dialog(form_nivel_completado)
            
    def update_sonidos(self, lista_eventos):
        self.volumen_musica, self.volumen_sonidos = self.cargar_configuracion_audio()
        for item in self.nivel.items:
            if isinstance(item, Recompensa):
                item.sonido_moneda.set_volume(self.volumen_sonidos)
                item.sonido_corazon.set_volume(self.volumen_sonidos)
                item.sonido_kunai.set_volume(self.volumen_sonidos)

        for enemigo in self.nivel.enemigos:
            enemigo.sonido_proyectil.set_volume(self.volumen_sonidos)
            enemigo.sonido_golpe_espada.set_volume(self.volumen_sonidos)
            enemigo.sonido_personaje_dolor.set_volume(self.volumen_sonidos)
        
        self.nivel.jugador.sonido_proyectil.set_volume(self.volumen_sonidos)
        self.nivel.jugador.sonido_golpe_espada.set_volume(self.volumen_sonidos)
        self.nivel.jugador.sonido_personaje_dolor.set_volume(self.volumen_sonidos)