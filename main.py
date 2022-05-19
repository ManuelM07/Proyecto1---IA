matriz = [[5, 0, 0], # toma la nave 
          [4, 0, 0], # consumido 2, 1, 0
          [1, 0, 0]] # si el padre tiene nave -> 
nodo_padre = None

x = 0
y = 0
cantidad_item = 5
nodos_expandidos = 5
profundidad = 0
total_items = 6
tiene_nave = False

def costo(peso, nave) -> int:
    if peso == 6 and not nave:
        return 4
    else:
        return 1
