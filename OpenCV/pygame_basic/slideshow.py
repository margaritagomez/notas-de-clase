# -*- coding: utf-8 -*-

"""
Ejemplo de visualización de imágenes en pygame.
"""

# 1. Importación de librerías

import cv2  # OpenCV
import glob  # Glob: Librería para listar archivos
import time  # Control de tiempo
import pygame # pygame
import numpy as np  # numpy
from pygame.locals import *  # Todas las teclas y eventos de pygame
import matplotlib.image as mpimg  # Rutinas de entrada/salida de imágenes


# 2. Rutina principal
def main():
    """
    Rutina principal
    """
    fps = 1  # 60 fotogramas por segundo
    finish = False  # El programa no ha finalizado
    pygame.init()  # Se inicializa pygame

    files = glob.glob('../img/slideshow/*.jpg')  # Se recuperan todas las imágenes JPEG
    cur_img = 0  # Índice de la imagen actual
    img = mpimg.imread(files[0])  # Se carga la primera imagen

    h, w, c = img.shape  # Se obtienen las dimensiones de la imagen
    screen = pygame.display.set_mode((w, h))  # Se define el tamaño de la ventana
    pygame.display.set_caption('Slideshow')  # Se define el título de la ventana

    clock = pygame.time.Clock()  # Control de fotogramas
    while not finish:  # Mientras no haya finalizado
        surf = pygame.surfarray.make_surface(np.rot90(img))  # Se carga la imagen a una superficie
        screen.blit(surf, (0, 0))  # Se muestra la superficie en la ventana
        pygame.display.update()  # Se muestra la imagen en pantalla
        clock.tick(fps)  # Cuenta de fotogramas

        cur_img = (cur_img + 1) % len(files)  # Se aumenta el índice
        img = mpimg.imread(files[cur_img])  # Se carga la siguiente imagen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Si el usuario cierra la ventana
                finish = True


# 3. Punto de entrada a la aplicación
if __name__ == '__main__':
    main()
