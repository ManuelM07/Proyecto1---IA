import numpy as np
import functools

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
        self.heuristica = 0
        self.tipo_nave = 0
        self.nave = nave
        self.combustible = combustible
        self.estado = self.validar_direcciones(x, y)
        self.cantidad_item = cantidad_item
        self.item_encontrado = False

    """ método que comprueba si este nodo es meta, True si es meta, False en caso contrario. """
    def es_meta(self) -> bool:
        return self.cantidad_item == total_items

    '''
    método para obtener (si corresponde) el elemento que se 
    encuentra en la posición actual del nodo (una nave o un ítem).
    '''
    def actualizar_estado_casilla(self) -> None: 
        casilla_actual = self.matriz[self.x][self.y]

        if casilla_actual == 3 or casilla_actual == 4:
            self.tipo_nave = 3 if casilla_actual == 3 else 4 # casilla 3 -> nave1, casilla 4 -> nave2
            self.combustible = 10 if casilla_actual == 3 else 20
            self.nave = True
        elif casilla_actual == 5: # encuentra el item
            self.cantidad_item += 1
            self.item_encontrado = True
        if casilla_actual == 3 or casilla_actual == 4 or casilla_actual == 5:
            self.matriz[self.x][self.y] = 0 
        
        # se calcula el costo del movimiento.
        if casilla_actual == 6 and not self.nave:
            self.costo += 4
        else:
            self.costo += 1

    """ método para saber si el nodo hijo tiene o no nave. """
    def validar_nave(self) -> None:
        if self.nave:  
            nuevo_combustible = self.combustible - 1 #combustible del hijo.
            tiene_nave = nuevo_combustible != 0 #true o false
            return tiene_nave, nuevo_combustible if tiene_nave else 0 # se retorna el booleano para saber si tiene nave y el nuevo combustible.
        else:
            return False, 0

    '''
    método que retorna una lista con parejas (operador, mundo), correspondientes al camino
    para llegar a la meta y el estado del mundo en cada nodo.
    '''
    def encontrar_camino(self) -> list:
        if self.nodo_padre is None:
            return []
        else:    
            return [[self.operador, self.matriz, self.combustible, self.costo, self.heuristica]] + self.nodo_padre.encontrar_camino() 

    """ método que verifica que en cada dirección no se salga de la matriz. """
    def validar_direcciones(self, x, y):
        izquierda = self.matriz[self.x][self.y-1] if y > 0 else -1
        derecha = self.matriz[self.x][self.y+1] if y < len(self.matriz)-1 else -1
        arriba = self.matriz[self.x-1][self.y] if x > 0 else -1
        abajo = self.matriz[self.x+1][self.y] if x < len(self.matriz)-1 else -1

        return  {
            "izquierda": izquierda, 
            "derecha": derecha, 
            "arriba": arriba,
            "abajo": abajo,    
        } 
    """ método para que los nodos se puedan comparar en la cola de prioridad. """
    def __lt__(self, other):
        return ((self.heuristica + self.costo) < (other.heuristica + other.costo))