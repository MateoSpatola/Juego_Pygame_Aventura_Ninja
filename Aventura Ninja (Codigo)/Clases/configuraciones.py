import pygame

def reescalar_imagenes(lista_imagenes, tamaño):
        for imagen in range(len(lista_imagenes)):
            lista_imagenes[imagen] = pygame.transform.scale(lista_imagenes[imagen], tamaño)

def girar_imagenes(lista_original: list, flip_x: bool, flip_y: bool) -> list:
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

#PERSONAJE
personaje_quieto_derecha = [pygame.image.load("Recursos\Personajes\Jugador\Idle\Idle__000.png"),
                    pygame.image.load("Recursos\Personajes\Jugador\Idle\Idle__001.png"),
                    pygame.image.load("Recursos\Personajes\Jugador\Idle\Idle__002.png"),
                    pygame.image.load("Recursos\Personajes\Jugador\Idle\Idle__003.png"),
                    pygame.image.load("Recursos\Personajes\Jugador\Idle\Idle__004.png"),
                    pygame.image.load("Recursos\Personajes\Jugador\Idle\Idle__005.png"),
                    pygame.image.load("Recursos\Personajes\Jugador\Idle\Idle__006.png"),
                    pygame.image.load("Recursos\Personajes\Jugador\Idle\Idle__007.png"),
                    pygame.image.load("Recursos\Personajes\Jugador\Idle\Idle__008.png"),
                    pygame.image.load("Recursos\Personajes\Jugador\Idle\Idle__009.png")]
personaje_quieto_izquierda = girar_imagenes(personaje_quieto_derecha, True, False)

personaje_camina_derecha = [pygame.image.load("Recursos\Personajes\Jugador\Run\Run__000.png"),
                            pygame.image.load("Recursos\Personajes\Jugador\Run\Run__001.png"),
                            pygame.image.load("Recursos\Personajes\Jugador\Run\Run__002.png"),
                            pygame.image.load("Recursos\Personajes\Jugador\Run\Run__003.png"),
                            pygame.image.load("Recursos\Personajes\Jugador\Run\Run__004.png"),
                            pygame.image.load("Recursos\Personajes\Jugador\Run\Run__005.png"),
                            pygame.image.load("Recursos\Personajes\Jugador\Run\Run__006.png"),
                            pygame.image.load("Recursos\Personajes\Jugador\Run\Run__007.png"),
                            pygame.image.load("Recursos\Personajes\Jugador\Run\Run__008.png"),
                            pygame.image.load("Recursos\Personajes\Jugador\Run\Run__009.png")]
personaje_camina_izquierda = girar_imagenes(personaje_camina_derecha, True, False)

personaje_salta_derecha = [pygame.image.load("Recursos\Personajes\Jugador\Jump\Jump__000.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Jump\Jump__001.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Jump\Jump__002.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Jump\Jump__003.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Jump\Jump__004.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Jump\Jump__005.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Jump\Jump__006.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Jump\Jump__007.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Jump\Jump__008.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Jump\Jump__009.png")]
personaje_salta_izquierda = girar_imagenes(personaje_salta_derecha, True, False)


personaje_lanza_derecha = [pygame.image.load("Recursos\Personajes\Jugador\Throw\Throw__000.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Throw\Throw__001.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Throw\Throw__002.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Throw\Throw__003.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Throw\Throw__004.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Throw\Throw__005.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Throw\Throw__006.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Throw\Throw__007.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Throw\Throw__008.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Throw\Throw__009.png")]
personaje_lanza_izquierda = girar_imagenes(personaje_lanza_derecha, True, False)

personaje_ataca_derecha = [pygame.image.load("Recursos\Personajes\Jugador\Attack\Attack__000.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Attack\Attack__001.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Attack\Attack__002.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Attack\Attack__003.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Attack\Attack__004.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Attack\Attack__005.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Attack\Attack__006.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Attack\Attack__007.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Attack\Attack__008.png"),
                pygame.image.load("Recursos\Personajes\Jugador\Attack\Attack__009.png")]
personaje_ataca_izquierda = girar_imagenes(personaje_ataca_derecha, True, False)

reduccion = 5
reescalar_imagenes(personaje_quieto_derecha, (232/reduccion, 439/reduccion))
reescalar_imagenes(personaje_quieto_izquierda, (232/reduccion, 439/reduccion))
reescalar_imagenes(personaje_camina_derecha, (362/reduccion, 439/reduccion))
reescalar_imagenes(personaje_camina_izquierda, (362/reduccion, 439/reduccion))
reescalar_imagenes(personaje_salta_derecha, (362/reduccion, 439/reduccion))
reescalar_imagenes(personaje_salta_izquierda, (362/reduccion, 439/reduccion))
reescalar_imagenes(personaje_lanza_derecha, (377/reduccion, 439/reduccion))
reescalar_imagenes(personaje_lanza_izquierda, (377/reduccion, 439/reduccion))
reescalar_imagenes(personaje_ataca_derecha, (536/reduccion, 495/reduccion))
reescalar_imagenes(personaje_ataca_izquierda, (536/reduccion, 495/reduccion))

diccionario_animaciones_personaje = {"quieto_derecha" : personaje_quieto_derecha,
                                    "quieto_izquierda" : personaje_quieto_izquierda,
                                    "camina_derecha" : personaje_camina_derecha,
                                    "camina_izquierda" : personaje_camina_izquierda,
                                    "salta_derecha" : personaje_salta_derecha,
                                    "salta_izquierda" : personaje_salta_izquierda,
                                    "lanza_derecha" : personaje_lanza_derecha,
                                    "lanza_izquierda" : personaje_lanza_izquierda,
                                    "ataca_derecha" : personaje_ataca_derecha,
                                    "ataca_izquierda" : personaje_ataca_izquierda,}

#PLATAFORMAS
plataforma_piedra = [pygame.image.load("Recursos\Plataformas\Piedra.png")]
plataforma_pasto = [pygame.image.load("Recursos\Plataformas\Pasto.png")]

reescalar_imagenes(plataforma_pasto, (40, 40))
reescalar_imagenes(plataforma_piedra, (40, 40))

diccionario_plataformas = {"pasto" : plataforma_pasto,
                            "piedra" : plataforma_piedra}

#ITEMS
#RECOMPENSAS
recompensa_moneda = [pygame.image.load("Recursos\Items\Recompenzas\Moneda/0.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/0.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/0.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/1.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/1.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/1.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/2.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/2.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/2.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/3.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/3.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/3.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/4.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/4.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/4.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/5.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/5.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Moneda/5.png")]

recompensa_corazon = [pygame.image.load("Recursos\Items\Recompenzas\Corazon/0.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Corazon/0.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Corazon/0.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Corazon/1.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Corazon/1.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Corazon/1.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Corazon/2.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Corazon/2.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Corazon/2.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Corazon/3.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Corazon/3.png"),
            pygame.image.load("Recursos\Items\Recompenzas\Corazon/3.png")]

recompensa_kunai = [pygame.image.load("Recursos\Items\Recompenzas\Kunai\Kunai.png")]

reescalar_imagenes(recompensa_moneda, (20, 20))
reescalar_imagenes(recompensa_corazon, (40, 40))
reescalar_imagenes(recompensa_kunai, (12, 40))

diccionario_recompensas = {"moneda" : recompensa_moneda,
                            "corazon" : recompensa_corazon,
                            "kunai" : recompensa_kunai}


#TRAMPAS
trampa_pinchos = [pygame.image.load("Recursos\Items\Trampas\Pinchos/0.png"),
            pygame.image.load("Recursos\Items\Trampas\Pinchos/0.png"),
            pygame.image.load("Recursos\Items\Trampas\Pinchos/1.png"),
            pygame.image.load("Recursos\Items\Trampas\Pinchos/1.png"),
            pygame.image.load("Recursos\Items\Trampas\Pinchos/2.png"),
            pygame.image.load("Recursos\Items\Trampas\Pinchos/2.png"),
            pygame.image.load("Recursos\Items\Trampas\Pinchos/3.png"),
            pygame.image.load("Recursos\Items\Trampas\Pinchos/3.png"),
            pygame.image.load("Recursos\Items\Trampas\Pinchos/4.png"),
            pygame.image.load("Recursos\Items\Trampas\Pinchos/4.png"),
            pygame.image.load("Recursos\Items\Trampas\Pinchos/4.png")]

reescalar_imagenes(trampa_pinchos, (20, 50))

diccionario_trampas = {"pinchos" : trampa_pinchos}


#PROYECTIL
proyectil_ninja_derecha = [pygame.image.load("Recursos\Items\Proyectiles\Proyectil_Ninja\Kunai.png")]
proyectil_ninja_izquierda = girar_imagenes(proyectil_ninja_derecha, True, False)

proyectil_Samurai_Mek_derecha = [pygame.image.load("Recursos\Items\Proyectiles\Proyectil_Samurai_Mek\Bullet_000.png"),
                                pygame.image.load("Recursos\Items\Proyectiles\Proyectil_Samurai_Mek\Bullet_001.png"),
                                pygame.image.load("Recursos\Items\Proyectiles\Proyectil_Samurai_Mek\Bullet_002.png"),
                                pygame.image.load("Recursos\Items\Proyectiles\Proyectil_Samurai_Mek\Bullet_003.png"),
                                pygame.image.load("Recursos\Items\Proyectiles\Proyectil_Samurai_Mek\Bullet_004.png")]
proyectil_Samurai_Mek_izquierda = girar_imagenes(proyectil_Samurai_Mek_derecha, True, False)

reescalar_imagenes(proyectil_ninja_derecha, (40, 12))
reescalar_imagenes(proyectil_ninja_izquierda, (40, 12))
reescalar_imagenes(proyectil_Samurai_Mek_derecha, (40, 12))
reescalar_imagenes(proyectil_Samurai_Mek_izquierda, (40, 12))

diccionario_proyectiles = {"proyectil_ninja_derecha" : proyectil_ninja_derecha,
                        "proyectil_ninja_izquierda" : proyectil_ninja_izquierda,
                        "proyectil_Samurai_Mek_derecha" : proyectil_Samurai_Mek_derecha,
                        "proyectil_Samurai_Mek_izquierda" : proyectil_Samurai_Mek_izquierda}


#ENEMIGOS
ninja_enemigo_mujer_quieto_derecha = [pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Idle\Idle__000.png"),
                    pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Idle\Idle__001.png"),
                    pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Idle\Idle__002.png"),
                    pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Idle\Idle__003.png"),
                    pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Idle\Idle__004.png"),
                    pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Idle\Idle__005.png"),
                    pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Idle\Idle__006.png"),
                    pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Idle\Idle__007.png"),
                    pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Idle\Idle__008.png"),
                    pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Idle\Idle__009.png")]
ninja_enemigo_mujer_quieto_izquierda = girar_imagenes(ninja_enemigo_mujer_quieto_derecha, True, False)

ninja_enemigo_mujer_camina_derecha = [pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Run\Run__000.png"),
                            pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Run\Run__001.png"),
                            pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Run\Run__002.png"),
                            pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Run\Run__003.png"),
                            pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Run\Run__004.png"),
                            pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Run\Run__005.png"),
                            pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Run\Run__006.png"),
                            pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Run\Run__007.png"),
                            pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Run\Run__008.png"),
                            pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Run\Run__009.png")]
ninja_enemigo_mujer_camina_izquierda = girar_imagenes(ninja_enemigo_mujer_camina_derecha, True, False)

ninja_enemigo_mujer_salta_derecha = [pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Jump\Jump__000.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Jump\Jump__001.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Jump\Jump__002.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Jump\Jump__003.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Jump\Jump__004.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Jump\Jump__005.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Jump\Jump__006.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Jump\Jump__007.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Jump\Jump__008.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Jump\Jump__009.png")]
ninja_enemigo_mujer_salta_izquierda = girar_imagenes(ninja_enemigo_mujer_salta_derecha, True, False)


ninja_enemigo_mujer_lanza_derecha = [pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Throw\Throw__000.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Throw\Throw__001.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Throw\Throw__002.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Throw\Throw__003.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Throw\Throw__004.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Throw\Throw__005.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Throw\Throw__006.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Throw\Throw__007.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Throw\Throw__008.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Throw\Throw__009.png")]
ninja_enemigo_mujer_lanza_izquierda = girar_imagenes(ninja_enemigo_mujer_lanza_derecha, True, False)

ninja_enemigo_mujer_ataca_derecha = [pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Attack\Attack__000.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Attack\Attack__001.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Attack\Attack__002.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Attack\Attack__003.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Attack\Attack__004.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Attack\Attack__005.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Attack\Attack__006.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Attack\Attack__007.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Attack\Attack__008.png"),
                pygame.image.load("Recursos\Personajes/Ninja_Enemigo_Mujer\Attack\Attack__009.png")]
ninja_enemigo_mujer_ataca_izquierda = girar_imagenes(ninja_enemigo_mujer_ataca_derecha, True, False)

reduccion = 5
reescalar_imagenes(ninja_enemigo_mujer_quieto_derecha, (232/reduccion, 439/reduccion))
reescalar_imagenes(ninja_enemigo_mujer_quieto_izquierda, (232/reduccion, 439/reduccion))
reescalar_imagenes(ninja_enemigo_mujer_camina_derecha, (362/reduccion, 439/reduccion))
reescalar_imagenes(ninja_enemigo_mujer_camina_izquierda, (362/reduccion, 439/reduccion))
reescalar_imagenes(ninja_enemigo_mujer_salta_derecha, (362/reduccion, 439/reduccion))
reescalar_imagenes(ninja_enemigo_mujer_salta_izquierda, (362/reduccion, 439/reduccion))
reescalar_imagenes(ninja_enemigo_mujer_lanza_derecha, (377/reduccion, 439/reduccion))
reescalar_imagenes(ninja_enemigo_mujer_lanza_izquierda, (377/reduccion, 439/reduccion))
reescalar_imagenes(ninja_enemigo_mujer_ataca_derecha, (536/reduccion, 495/reduccion))
reescalar_imagenes(ninja_enemigo_mujer_ataca_izquierda, (536/reduccion, 495/reduccion))

diccionario_animaciones_ninja_enemigo_mujer = {"quieto_derecha" : ninja_enemigo_mujer_quieto_derecha,
                                    "quieto_izquierda" : ninja_enemigo_mujer_quieto_izquierda,
                                    "camina_derecha" : ninja_enemigo_mujer_camina_derecha,
                                    "camina_izquierda" : ninja_enemigo_mujer_camina_izquierda,
                                    "salta_derecha" : ninja_enemigo_mujer_salta_derecha,
                                    "salta_izquierda" : ninja_enemigo_mujer_salta_izquierda,
                                    "lanza_derecha" : ninja_enemigo_mujer_lanza_derecha,
                                    "lanza_izquierda" : ninja_enemigo_mujer_lanza_izquierda,
                                    "ataca_derecha" : ninja_enemigo_mujer_ataca_derecha,
                                    "ataca_izquierda" : ninja_enemigo_mujer_ataca_izquierda}


#BOSS SAMURAI MEK
boss_samurai_mek_quieto_derecha = [pygame.image.load("Recursos\Personajes\Samurai_Mek\Idle\Idle (1).png"),
                    pygame.image.load("Recursos\Personajes\Samurai_Mek\Idle\Idle (2).png"),
                    pygame.image.load("Recursos\Personajes\Samurai_Mek\Idle\Idle (3).png"),
                    pygame.image.load("Recursos\Personajes\Samurai_Mek\Idle\Idle (4).png"),
                    pygame.image.load("Recursos\Personajes\Samurai_Mek\Idle\Idle (5).png"),
                    pygame.image.load("Recursos\Personajes\Samurai_Mek\Idle\Idle (6).png"),
                    pygame.image.load("Recursos\Personajes\Samurai_Mek\Idle\Idle (7).png"),
                    pygame.image.load("Recursos\Personajes\Samurai_Mek\Idle\Idle (8).png"),
                    pygame.image.load("Recursos\Personajes\Samurai_Mek\Idle\Idle (9).png"),
                    pygame.image.load("Recursos\Personajes\Samurai_Mek\Idle\Idle (10).png")]
boss_samurai_mek_quieto_izquierda = girar_imagenes(boss_samurai_mek_quieto_derecha, True, False)

boss_samurai_mek_camina_derecha = [pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (1).png"),
                            pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (1).png"),
                            pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (2).png"),
                            pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (2).png"),
                            pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (3).png"),
                            pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (3).png"),
                            pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (4).png"),
                            pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (4).png"),
                            pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (5).png"),
                            pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (5).png"),
                            pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (6).png"),
                            pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (6).png"),
                            pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (7).png"),
                            pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (7).png"),
                            pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (8).png"),
                            pygame.image.load("Recursos\Personajes\Samurai_Mek\Run\Run (8).png")]
boss_samurai_mek_camina_izquierda = girar_imagenes(boss_samurai_mek_camina_derecha, True, False)

boss_samurai_mek_salta_derecha = [pygame.image.load("Recursos\Personajes\Samurai_Mek\Jump\Jump (1).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Jump\Jump (2).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Jump\Jump (3).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Jump\Jump (4).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Jump\Jump (5).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Jump\Jump (6).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Jump\Jump (7).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Jump\Jump (8).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Jump\Jump (9).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Jump\Jump (10).png")]
boss_samurai_mek_salta_izquierda = girar_imagenes(boss_samurai_mek_salta_derecha, True, False)


boss_samurai_mek_lanza_derecha = [pygame.image.load("Recursos\Personajes\Samurai_Mek\Shoot\Shoot (1).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Shoot\Shoot (1).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Shoot\Shoot (2).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Shoot\Shoot (2).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Shoot\Shoot (3).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Shoot\Shoot (3).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Shoot\Shoot (4).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Shoot\Shoot (4).png")]
boss_samurai_mek_lanza_izquierda = girar_imagenes(boss_samurai_mek_lanza_derecha, True, False)

boss_samurai_mek_ataca_derecha = [pygame.image.load("Recursos\Personajes\Samurai_Mek\Attack\Melee (1).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Attack\Melee (2).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Attack\Melee (3).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Attack\Melee (4).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Attack\Melee (5).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Attack\Melee (6).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Attack\Melee (7).png"),
                pygame.image.load("Recursos\Personajes\Samurai_Mek\Attack\Melee (8).png")]
boss_samurai_mek_ataca_izquierda = girar_imagenes(boss_samurai_mek_ataca_derecha, True, False)

reduccion = 5
reescalar_imagenes(boss_samurai_mek_quieto_derecha, (273/reduccion, 468/reduccion))
reescalar_imagenes(boss_samurai_mek_quieto_izquierda, (273/reduccion, 468/reduccion))
reescalar_imagenes(boss_samurai_mek_camina_derecha, (366/reduccion, 468/reduccion))
reescalar_imagenes(boss_samurai_mek_camina_izquierda, (366/reduccion, 468/reduccion))
reescalar_imagenes(boss_samurai_mek_salta_derecha, (400/reduccion, 468/reduccion))
reescalar_imagenes(boss_samurai_mek_salta_izquierda, (400/reduccion, 468/reduccion))
reescalar_imagenes(boss_samurai_mek_lanza_derecha, (360/reduccion, 468/reduccion))
reescalar_imagenes(boss_samurai_mek_lanza_izquierda, (360/reduccion, 468/reduccion))
reescalar_imagenes(boss_samurai_mek_ataca_derecha, (517/reduccion, 546/reduccion))
reescalar_imagenes(boss_samurai_mek_ataca_izquierda, (517/reduccion, 546/reduccion))

diccionario_animaciones_boss_samurai_mek = {"quieto_derecha" : boss_samurai_mek_quieto_derecha,
                                    "quieto_izquierda" : boss_samurai_mek_quieto_izquierda,
                                    "camina_derecha" : boss_samurai_mek_camina_derecha,
                                    "camina_izquierda" : boss_samurai_mek_camina_izquierda,
                                    "salta_derecha" : boss_samurai_mek_salta_derecha,
                                    "salta_izquierda" : boss_samurai_mek_salta_izquierda,
                                    "lanza_derecha" : boss_samurai_mek_lanza_derecha,
                                    "lanza_izquierda" : boss_samurai_mek_lanza_izquierda,
                                    "ataca_derecha" : boss_samurai_mek_ataca_derecha,
                                    "ataca_izquierda" : boss_samurai_mek_ataca_izquierda}