from main import nodos_expandidos, total_items

operadores = ["arriba", "abajo", "izquierda", "derecha"]

class Nodo:
    
    def __init__(self, matriz, x, y, nodo_padre, operador, profundidad, costo, nave, combustible, cantidad_item) -> None:
        self.matriz = matriz
        self.x = x
        self.y = y
        self.nodo_padre = nodo_padre
        self.operador = operador
        self.profundidad = profundidad
        self.costo = costo
        self.nave = nave
        self.combustible = combustible
        self.estado = {
            "izquierda": self.matriz[self.x-1][self.y], # 6 -> 4 
            "derecha": self.matriz[self.x+1][self.y], 
            "arriba": self.matriz[self.x][self.y-1],
            "abajo": self.matriz[self.x][self.y+1],    
        } # operador, si tiene o no tiene nave o gasolina
        self.cantidad_item = cantidad_item


    def __eq__(self, other) -> bool:
        return self.nave == other.nave


    def expandir_nodo(self) -> bool:
        if not self.cantidad_item == total_items:
            return False 
        else:
            return True

    
    def validar_casilla(self, siguiente_casilla) -> bool: # self.matriz[self.x][self.y-1]
        if siguiente_casilla != 1:
            if siguiente_casilla == 3 or siguiente_casilla == 4: # valida si es una nave
                self.combustible = 10 if siguiente_casilla == 3 else 20
                self.matriz[self.x][self.y-1] = 0
                self.nave = True
            return True
        else:
            return False


    def validar_nave(self) -> None:
        if self.nave:  
            self.combustible -= 1
            if not self.combustible:
                self.nave = False   
        


matriz1 = [
    [0,0,0,0,0],
    [0,5,0,2,1],
    [0,1,1,1,3],
]

