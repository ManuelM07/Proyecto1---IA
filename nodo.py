#from main import nodos_expandidos, total_items

from numpy import matrix


total_items = 2
operadores = ["derecha", "arriba", "abajo", "izquierda"]

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
        self.estado = self.validar_direcciones(x, y)
        self.cantidad_item = cantidad_item


    def __eq__(self, other) -> bool:
        return self.nave == other.nave


    def es_meta(self) -> bool:
        print(self.cantidad_item)
        if not self.cantidad_item == total_items:
            return False 
        else:
            return True

    
    def validar_casilla(self, x, y) -> bool: # self.matriz[self.x][self.y-1]
        siguiente_casilla = self.matriz[x][y]

        if siguiente_casilla != 1:
            if siguiente_casilla == 3 or siguiente_casilla == 4: # valida si es una nave
                self.combustible = 10 if siguiente_casilla == 3 else 20
                self.matriz[x][y] = 0
                self.nave = True
            elif siguiente_casilla == 5:
                self.matriz[x][y] = 0
                self.cantidad_item += 1
                print("Yeah")


            return True

        else:
            return False


    def validar_nave(self) -> None:
        if self.nave:  
            self.combustible -= 1
            if not self.combustible:
                self.nave = False   


    def encontrar_camino(self) -> list:
        if self.nodo_padre is None:
            return []
        else:
            return [self.operador] + self.nodo_padre.encontrar_camino() 

        
    def validar_direcciones(self, x, y):
        izquierda = self.matriz[self.x-1][self.y] if x > 0 else -1
        derecha = self.matriz[self.x+1][self.y] if x < len(self.matriz)-1 else -1
        arriba = self.matriz[self.x][self.y-1] if y > 0 else -1
        abajo = self.matriz[self.x][self.y+1] if y < len(self.matriz)-1 else -1

        return  {
            "izquierda": izquierda, # 6 -> 4 
            "derecha": derecha, 
            "arriba": arriba,
            "abajo": abajo,    
        } # operador, si tiene o no tiene nave o gasolina


         


matriz1 = [
    [0,0,0,0,0],
    [0,5,0,2,1],
    [0,1,1,1,3],
]

