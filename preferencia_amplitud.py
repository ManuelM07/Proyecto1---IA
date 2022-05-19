from nodo import Nodo, operadores

cola = []

def preferencia_amplitud(matriz, x, y):
    nodo_raiz = Nodo(matriz, x, y, None, 0, 0, False, 0)
    while True:
        expandir_nodo(nodo_raiz)

    # (matriz, x, y, nodo_padre, operador, profundidad, costo, nave, combustible)


def expandir_nodo(nodo_padre):
    if nodo_padre.expandir_nodo():
        return True
    else:
        crear_hijos()


def crear_hijos(nodo_padre):
        x = nodo_padre.x
        y = nodo_padre.y
        cola = cola[1:]
        derecha = nodo_padre[x+1][y]
        izquierda = nodo_padre[x-1][y]
        abajo = nodo_padre[x][y+1]
        arriba = nodo_padre[x][y-1]
        aux_profundidad = nodo_padre.profundidad + 1 #

        for op in operadores:
            if (op == "arriba" and nodo_padre.y > 0 and arriba != 1): 
                nodo_padre.validar_nave()
                if (nodo_padre.operador == "abajo" and (nodo_padre.nave != nodo_padre.nodo_padre.nave) or # se verifica que si se puede devolver
                    (nodo_padre.operador != "abajo" and nodo_padre.validar_casilla(arriba))): # O verifica que no haya un muro en la siguiente casilla y se verifica que no se regrese
                    new_nodo = Nodo(nodo_padre.matriz, nodo_padre.x, nodo_padre.y-1, nodo_padre, "arriba", aux_profundidad, 0, nodo_padre.nave, nodo_padre.combustible)
                    cola.append(new_nodo)




            elif (op == "abajo" and nodo_padre.y < len(nodo_padre.matriz) and abajo != 1) and (nodo_padre.operador != "arriba" or (nodo_padre.nave and (nodo_padre.combustible == 10 or nodo_padre.combustible == 20))): 
                pass
            elif op == "izquierda" and nodo_padre.x > 0 and izquierda != 1: 
                pass
            elif op == "derecha" and nodo_padre.x < len(nodo_padre.matriz) and derecha != 1: 
                    pass