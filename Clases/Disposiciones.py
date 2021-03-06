from math import log, atan2, cos, sin
import pygame
import random

from Clases.Arista import Arista
from Clases.Grafo import Grafo
from Clases.Nodo import Nodo

WIDTH, HEIGHT   = 1700, 1000
BORDER          = 15
WIN             = pygame.display.set_mode((WIDTH, HEIGHT))

# colores
BG              = (251, 241, 199)
BLUE            = (69, 133, 136)
BLACK           = (40, 40, 40)
RED             = (157, 0, 6)

ITERS           = 1500
FPS             = 40
NODE_RADIUS     = 10
DIST_MIN        = (min(WIDTH, HEIGHT)) // 35
NODE_MIN_WIDTH  = 25
NODE_MIN_HEIGHT = 25
NODE_MAX_WIDTH  = WIDTH - 25
NODE_MAX_HEIGHT = HEIGHT - 25


c1 = 1.65
c2 = 0.9
c3 = 0.4
c4 = 0.6


def spring(g):
    run = True
    clock = pygame.time.Clock()

    init_nodes(g)
    dibujar_aristas(g)
    dibujar_nodos(g)

    i = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if i > ITERS:
            continue

        WIN.fill(BG)
        update_nodes(g)
        dibujar_aristas(g)
        dibujar_nodos(g)
        pygame.display.update()
        i += 1

    pygame.quit()
    return


def init_nodes(g):
    for node in g.V.values():
        x = random.randrange(NODE_MIN_WIDTH, NODE_MAX_WIDTH)
        y = random.randrange(NODE_MIN_HEIGHT, NODE_MAX_HEIGHT)
        node.attrs['coords'] = [x, y]

    return

def update_nodes(g):
    for node in g.V.values():
        x_attraction = 0
        y_attraction = 0
        x_node, y_node = node.attrs['coords']

        for other in node.connected_to:
            x_other, y_other = g.V[other].attrs['coords']
            d = ((x_node - x_other) ** 2 + (y_node - y_other)**2) ** 0.5

            # defining minimum distance
            if d < DIST_MIN:
                continue
            attraction = c1 * log(d / c2)
            angle = atan2(y_other - y_node, x_other - x_node)
            x_attraction += attraction * cos(angle)
            y_attraction += attraction * sin(angle)

        not_connected = (other for other in g.V.values()
                         if (other.id not in node.connected_to and other != node))
        x_repulsion = 0
        y_repulsion = 0
        for other in not_connected:
            x_other, y_other = other.attrs['coords']
            d = ((x_node - x_other) ** 2 + (y_node - y_other)**2) ** 0.5
            if d == 0:
                continue
            repulsion = c3 / d ** 0.5
            angle = atan2(y_other - y_node, x_other - x_node)
            x_repulsion -= repulsion * cos(angle)
            y_repulsion -= repulsion * sin(angle)

        fx = x_attraction + x_repulsion
        fy = y_attraction + y_repulsion
        node.attrs['coords'][0] += c4 * fx
        node.attrs['coords'][1] += c4 * fy

        # Restrict for limits of window
        node.attrs['coords'][0] = max(node.attrs['coords'][0], NODE_MIN_WIDTH)
        node.attrs['coords'][1] = max(node.attrs['coords'][1], NODE_MIN_HEIGHT)
        node.attrs['coords'][0] = min(node.attrs['coords'][0], NODE_MAX_WIDTH)
        node.attrs['coords'][1] = min(node.attrs['coords'][1], NODE_MAX_HEIGHT)

    return


def dibujar_nodos(g):
    for node in g.V.values():
        pygame.draw.circle(WIN, BLUE, node.attrs['coords'], NODE_RADIUS - 3, 0)
        pygame.draw.circle(WIN, RED, node.attrs['coords'], NODE_RADIUS, 3)

    return


def dibujar_aristas(g):
    for edge in g.E:
        u, v = edge
        u_pos = g.V[u].attrs['coords']
        v_pos = g.V[v].attrs['coords']

        pygame.draw.line(WIN, BLACK, u_pos, v_pos, 1)

    return