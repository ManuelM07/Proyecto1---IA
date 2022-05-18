from main import nodos_expandidos, cantidad_item, total_items

operadores = ["arriba", "abajo", "izquierda", "derecha"]

class Nodo:
    
    def __init__(self, matriz, x, y, nodo_padre, operador, profundidad, costo, nave, combustible) -> None:
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
        } 

    def expandir_nodo(self):
        if not cantidad_item == total_items:
            return self.crear_hijos() 
        else:
            return True


    def crear_hijos(self, cola):
        cola = cola[1:]
        gasolina = 0

    # (matriz, x, y, nodo_padre, operador, profundidad, costo, nave, combustible)
        for op in operadores:
            if (op == "arriba" and self.y > 0 and self.matriz[self.x][self.y-1] != 1) and ( (self.nave and (self.combustible == 10 or self.combustible == 20))): 
                siguiente_casilla = self.matriz[self.x][self.y-1] # guarda el elemento de la proxima casilla
                if siguiente_casilla == 3 or siguiente_casilla == 4:
                    gasolina = 10 if siguiente_casilla == 3 else 20
                    self.matriz[self.x][self.y-1] == 0
                    nave = True
                cola.append(
                    self.matriz, self.x, self.y-1, "arriba", 
                )
            elif (op == "abajo" and self.y < len(self.matriz) and self.matriz[self.x][self.y+1] != 1) and (self.operador != "arriba" or (self.nave and (self.combustible == 10 or self.combustible == 20))): 
                pass
            elif op == "izquierda" and self.x > 0 and self.matriz[self.x-1][self.y] != 1: 
                pass
            elif op == "derecha" and self.x < len(self.matriz) and self.matriz[self.x+1][self.y] != 1: 
                pass

def costo(peso, nave):
    if peso == 6 and not nave:
        return 4
    else:
        return 1


matriz1 = [
    [0,0,0,0,0],
    [0,5,0,2,1],
    [0,1,1,1,3],
]


'''    def crear_nodo(self) -> dict:
        nodo = {"x": self.x, "y":self.y, 
        "estado": {
            "izquierda": self.matriz[self.x-1][self.y], # 6 -> 4 
            "derecha": self.matriz[self.x+1][self.y], 
            "arriba": self.matriz[self.x][self.y-1],
            "abajo": self.matriz[self.x][self.y+1],
            },
        "referencia": self.nodo_padre,
        "operador": self.operador,
        "profundidad": self.profundidad,
        "costo_ruta": self.costo,
        "nave": {"activo": self.nave, "combustible": self.combustible}
        }

        return nodo'''
# (matriz, x, y, nodo_padre, operador, profundidad, costo, nave, combustible) 