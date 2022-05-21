import pygame as pg
import sys
import numpy as np
from preferencia_amplitud import preferencia_amplitud
import time

n = 10 # matriz nxn
nombre_lectura = "mundo"
ancho = 640
alto = ancho
distancia = ancho // n
x0 = 0
y0 = 0
ticks = 2
'''
0 -> casilla libre
1 -> muro
2 -> punto de inicio
3 -> nave1
4 -> nave2
5 -> item 
6 -> aceite
'''
colores = {0:(255,255,255), 1:(150,75,0), 2:(0,230,230), 
            3:(0, 255, 0), 4:(204,204,255), 5:(255,255,0), 6:(255,0,0)}
'''
input()
Función para leer el archivo bajo el formato establecido en el proyecto. El
nombre se cambia en la variable global "nombreLectura". 
'''
""" def input():
    with open("src/"+nombreLectura+".txt", "r") as f:
        content = f.read().split('\n')
        mundo = []
        for i in range(n):
            fila = list(map(lambda x: int(x), content[i].split(" ")))
            mundo.append(fila)
        return mundo """

def input():
    global x0, y0

    with open(f"{nombre_lectura}.txt", "r") as f:
        content = f.read().split('\n')
        mundo = []
        for i in range(n):
            fila = list(map(lambda x: int(x), content[i].split(" ")))
            mundo.append(fila)
            try: 
                y0 = fila.index(2)
                x0 = i
            except ValueError:
                pass
        return np.array(mundo)

# configuración inicial de la pantalla
def setup():
    global pantalla 
    pg.init()
    pantalla = pg.display.set_mode((ancho, alto))
    pg.display.set_caption('Smart Robot')
    pantalla.fill((255,255,255)) 

#crear la cuadrícula
def grid():
    size = ancho
    x = 0
    y = 0
    for l in range(n+1):
        pg.draw.line(pantalla, (0,0,0), (x,0), (x,size))
        pg.draw.line(pantalla, (0,0,0), (0,y), (size,y))
        x += distancia
        y += distancia

# Se pinta el mundo
def pintarMundo(mundo):
    x = 0
    y = 0
    tam = distancia #tamaño de cada cuadro.
    for fila in mundo:
        for valor in fila:
            pg.draw.rect(pantalla, pg.__color_constructor(colores.get(valor)[0], # se pinta el cuadro dependiendo el número que tiene.
                                                          colores.get(valor)[1], 
                                                          colores.get(valor)[2], 
                                                          0), (x, y, tam, tam))            
            x += tam
        x = 0
        y += tam

class Robot():
    def __init__(self, posx, posy, color, tam):
        self.x = posx
        self.y = posy
        self.color = color
        self.tam = tam
    
    def pintar(self):
        pg.draw.rect(pantalla, (self.color['r'], # se pinta el cuadro dependiendo el número que tiene.
                                                      self.color['g'], 
                                                      self.color['b']), (self.x, self.y, self.tam, self.tam)) 
    def mover(self, direccion):
        if direccion == "izquierda":
            self.x -= self.tam
        elif direccion == "derecha":
            self.x += self.tam
        elif direccion == "arriba":
            self.y -= self.tam
        elif direccion == "abajo":
            self.y += self.tam

# bucle infinito para mostrar en patalla todos los elementos gráficos.
def mostrarJuego(resultado):
    i = len(resultado)-1
    while True:
        clock.tick(ticks) #establece 200 fps.
        for event in pg.event.get():
            if event.type == pg.QUIT: #para detener la ejecución al cerrar la ventana.
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    robot.mover("iz")
                elif event.key == pg.K_RIGHT:
                    robot.mover("de")
                elif event.key == pg.K_UP:
                    robot.mover("ar")
                elif event.key == pg.K_DOWN:
                    robot.mover("ab")
      
        if (i >= 0):            
            pintarMundo(resultado[i][1]) #se obtiene el mundo.
            """ 
            print("x: ", robot.x)
            print("y: ", robot.y) """
            robot.mover(resultado[i][0]) #se obtiene el operador. 
            robot.pintar()
        grid()
        pg.display.flip() #actualiza el mundo para mostrar nuevos cambios.
        i -= 1


def mostrar_mundo(matrix):
    for fila in matrix:
        print(fila)

setup()
mundo = input() #se carga la matriz del mundo.
robot = Robot(x0*distancia, y0*distancia,{'r':100, 'g':100, 'b':230}, distancia)
clock = pg.time.Clock() #reloj para manipular la velocidad de la ejecución.

#se muestra por primera vez el mundo
pintarMundo(mundo)
robot.pintar()
grid()
pg.display.flip()

start = time.perf_counter()
resultado = preferencia_amplitud(mundo, x0, y0)
end = time.perf_counter()
print("tiempo: ", end-start)
mostrarJuego(resultado)