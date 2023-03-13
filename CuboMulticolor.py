import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define los vértices del cubo
vertices = (
    ( 1, -1, -1),
    ( 1,  1, -1),
    (-1,  1, -1),
    (-1, -1, -1),
    ( 1, -1,  1),
    ( 1,  1,  1),
    (-1, -1,  1),
    (-1,  1,  1)
)

# Define las caras del cubo
caras = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

# Define los colores de las caras
colores = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,1,0),
    (1,0,1),
    (0,1,1)
)

def cubo():
    glBegin(GL_QUADS)
    for i, cara in enumerate(caras):
        glColor3fv(colores[i])
        for vertice in cara:
            glVertex3fv(vertices[vertice])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    # Configura la perspectiva
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # Configura la posición de la cámara
    glTranslatef(0.0,0.0,-5)

    # Inicia el bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Gira el cubo
        glRotatef(1, 3, 1, 1)

        # Limpia la pantalla y dibuja el cubo
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cubo()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
