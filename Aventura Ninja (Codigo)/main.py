import pygame, sys
from pygame.locals import *

from Clases.Formularios.GUI.GUI_form_menu_principal import FormMenuPrincipal

########################################################################################

#PANTALLA
ANCHO , ALTO = 1280, 720
TAMAÑO_PANTALLA = (ANCHO,ALTO)
FPS = 30

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)

pygame.display.set_caption("Aventura Ninja")
form_menu_principal = FormMenuPrincipal(PANTALLA, 300, 50, 680, 620, True, "Recursos\Formularios\interfaz.png")

while True:
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    form_menu_principal.update(lista_eventos)
    pygame.display.update()