import numpy as np

total_items = 2
operadores = ["derecha", "arriba", "izquierda", "abajo"]

class Nodo:
    
    def __init__(self, matriz, x, y, nodo_padre, operador, profundidad, costo, nave, combustible, cantidad_item) -> None:
        self.matriz = np.array(matriz)
        self.x = x
        self.y = y
        self.nodo_padre = nodo_padre
        self.operador = operador
        self.profundidad = profundidad
        self.costo = costo
        self.nave = nave
        self.combustible = combustible
        self.estado = self.validar_direcciones(x, y)
        self.cantidad_item = cantidad_item


    def es_meta(self) -> bool:
        if not self.cantidad_item == total_items:
            return False 
        else:
            return True

    
    def actualizar_estado_casilla(self) -> None: # self.matriz[self.x][self.y-1]
        casilla_actual = self.matriz[self.x][self.y]

        if casilla_actual == 3 or casilla_actual == 4: # valida si es una nave
            self.combustible = 10 if casilla_actual == 3 else 20
            self.matriz[self.x][self.y] = 0
            self.nave = True
        elif casilla_actual == 5:
            self.matriz[self.x][self.y] = 0
            self.cantidad_item += 1


    def validar_nave(self) -> None:
        if self.nave:  
            nuevo_combustible = self.combustible - 1
            return nuevo_combustible != 0 # True si tiene nave o False en caso contrario


    def encontrar_camino(self) -> list:
        if self.nodo_padre is None:
            return []
        else:    
            return [[self.operador, self.matriz]] + self.nodo_padre.encontrar_camino() 

        
    def validar_direcciones(self, x, y):
        izquierda = self.matriz[self.x][self.y-1] if y > 0 else -1
        derecha = self.matriz[self.x][self.y+1] if y < len(self.matriz)-1 else -1
        arriba = self.matriz[self.x-1][self.y] if x > 0 else -1
        abajo = self.matriz[self.x+1][self.y] if x < len(self.matriz)-1 else -1

        return  {
            "izquierda": izquierda, # 6 -> 4 
            "derecha": derecha, 
            "arriba": arriba,
            "abajo": abajo,    
        } 