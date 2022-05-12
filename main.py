matriz = [[5, 0, 0],
          [4, 0, 0], 
          [1, 0, 0]]
nodo_padre = None

x = 0
y = 0
cantidad_item = 0
nodos_expandidos = 0
profundidad = 0
total_items = 6
tiene_nave = False



"""nodo = {"x": 0, "y":0, 
    "estado": {
        "izquierda": matriz[x-1][y], 
        "derecha": matriz[x+1][y],
        "arriba": matriz[x][y-1],
        "abajo": matriz[x][y+1],
        },
    "referencia": nodo_padre
}"""

informacion_persona = {
    "dni": "199239494", 
    "nombre": {"p_nombre": "Pepito", "apellido": "Perez"},
    "edad": 17, 
}


def costo(peso, nave):
    if peso == 6 and not nave:
        return 4
    else:
        return 1
    



def crear_nodo(x, y, nodo_padre, operador, profundidad, costo, nave, combustible) -> dict:
    nodo = {"x": x, "y":y, 
    "estado": {
        "izquierda": matriz[x-1][y], # 6 -> 4 
        "derecha": matriz[x+1][y], 
        "arriba": matriz[x][y-1],
        "abajo": matriz[x][y+1],
        },
    "referencia": nodo_padre,
    "operador": operador,
    "profundidad": profundidad,
    "costo_ruta": costo,
    "nave": {"activo": nave, "combustible": combustible}
    }

    return nodo