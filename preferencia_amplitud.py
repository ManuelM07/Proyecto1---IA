from nodo import Nodo, operadores

cola = []

def preferencia_amplitud(matriz, x, y):
    global cola

    nodo_raiz = Nodo(matriz, x, y, None, None, 0, 0, False, 0, 0)
    cola.append(nodo_raiz)

    while True: # return, break 
        if cola == []:
            return "Falla"
        cabeza = cola[0]
        cola = cola[1:]

        if cabeza.es_meta():
            return cabeza.encontrar_camino()
        crear_hijos(cabeza)            

    # (self, matriz, x, y, nodo_padre, operador, profundidad, costo, nave, combustible, cantidad_item)


"""def expandir_nodo(nodo_padre):
    if nodo_padre.expandir_nodo():
        return True
    else:
        crear_hijos()"""


def crear_hijos(nodo_padre):
        global cola

        x = nodo_padre.x
        y = nodo_padre.y

        derecha = nodo_padre.estado["derecha"]
        izquierda = nodo_padre.estado["izquierda"]
        abajo = nodo_padre.estado["abajo"]
        arriba = nodo_padre.estado["arriba"]
        aux_profundidad = nodo_padre.profundidad + 1 #

        for op in operadores:
            if (op == "arriba" and arriba != -1 and arriba != 1): 
                nodo_padre.validar_nave()
                if (nodo_padre.operador == "abajo" and (nodo_padre.nave != nodo_padre.nodo_padre.nave) or # se verifica que si se puede devolver
                    (nodo_padre.operador != "abajo" and nodo_padre.validar_casilla(x, y-1))): # O verifica que no haya un muro en la siguiente casilla y se verifica que no se regrese
                    new_nodo = Nodo(nodo_padre.matriz, nodo_padre.x, nodo_padre.y-1, nodo_padre, "arriba", aux_profundidad, 0, nodo_padre.nave, nodo_padre.combustible, nodo_padre.cantidad_item)
                    cola.append(new_nodo)

            elif (op == "abajo" and abajo != -1 and abajo != 1) and (nodo_padre.operador != "arriba" or (nodo_padre.nave and (nodo_padre.combustible == 10 or nodo_padre.combustible == 20))): 
                nodo_padre.validar_nave()
                if (nodo_padre.operador == "arriba" and (nodo_padre.nave != nodo_padre.nodo_padre.nave) or # se verifica que si se puede devolver
                    (nodo_padre.operador != "arriba" and nodo_padre.validar_casilla(x, y+1))): # O verifica que no haya un muro en la siguiente casilla y se verifica que no se regrese
                    new_nodo = Nodo(nodo_padre.matriz, nodo_padre.x, nodo_padre.y+1, nodo_padre, "arriba", aux_profundidad, 0, nodo_padre.nave, nodo_padre.combustible, nodo_padre.cantidad_item)
                    cola.append(new_nodo)

            elif op == "izquierda" and izquierda != -1 and izquierda != 1:  #
                nodo_padre.validar_nave()
                if (nodo_padre.operador == "derecha" and (nodo_padre.nave != nodo_padre.nodo_padre.nave) or # se verifica que si se puede devolver
                    (nodo_padre.operador != "derecha" and nodo_padre.validar_casilla(x-1, y))): # O verifica que no haya un muro en la siguiente casilla y se verifica que no se regrese
                    new_nodo = Nodo(nodo_padre.matriz, nodo_padre.x-1, nodo_padre.y, nodo_padre, "arriba", aux_profundidad, 0, nodo_padre.nave, nodo_padre.combustible, nodo_padre.cantidad_item)
                    cola.append(new_nodo)

            elif op == "derecha" and derecha != -1 and derecha != 1: 
                print("derecha")
                nodo_padre.validar_nave()
                if (nodo_padre.operador == "izquierda" and (nodo_padre.nave != nodo_padre.nodo_padre.nave) or # se verifica que si se puede devolver
                    (nodo_padre.operador != "izquierda" and nodo_padre.validar_casilla(x+1, y))): # O verifica que no haya un muro en la siguiente casilla y se verifica que no se regrese
                    new_nodo = Nodo(nodo_padre.matriz, nodo_padre.x+1, nodo_padre.y, nodo_padre, "arriba", aux_profundidad, 0, nodo_padre.nave, nodo_padre.combustible, nodo_padre.cantidad_item)
                    cola.append(new_nodo)
