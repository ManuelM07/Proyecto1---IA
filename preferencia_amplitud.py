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

        cabeza.actualizar_estado_casilla()
        if cabeza.es_meta():
            return cabeza.encontrar_camino()    
        crear_hijos(cabeza)            


def crear_hijos(nodo_padre):
    global cola
    nave_hijo = nodo_padre.validar_nave()
    nuevo_combustible = nodo_padre.combustible-1 if nave_hijo else 0

    matriz_copia = nodo_padre.matriz.copy()
    x = nodo_padre.x
    y = nodo_padre.y

    derecha = nodo_padre.estado["derecha"]
    izquierda = nodo_padre.estado["izquierda"]
    abajo = nodo_padre.estado["abajo"]
    arriba = nodo_padre.estado["arriba"]
    aux_profundidad = nodo_padre.profundidad + 1 #

    for op in operadores:
        if (op == "arriba" and arriba != -1 and arriba != 1): 
            if (nodo_padre.operador == "abajo" and (nodo_padre.nave != nave_hijo) or # se verifica que si se puede devolver
                (nodo_padre.operador != "abajo" )): # O verifica que no haya un muro en la siguiente casilla y se verifica que no se regrese
                new_nodo = Nodo(matriz_copia, x-1, y, nodo_padre, "arriba", aux_profundidad, 0, nave_hijo, nuevo_combustible, nodo_padre.cantidad_item)
                cola.append(new_nodo)

        elif (op == "abajo" and abajo != -1 and abajo != 1) and (nodo_padre.operador != "arriba" ): 
            if (nodo_padre.operador == "arriba" and (nodo_padre.nave != nave_hijo) or # se verifica que si se puede devolver
                (nodo_padre.operador != "arriba" )): # O verifica que no haya un muro en la siguiente casilla y se verifica que no se regrese
                new_nodo = Nodo(matriz_copia, x+1, y, nodo_padre, "abajo", aux_profundidad, 0, nave_hijo, nuevo_combustible, nodo_padre.cantidad_item)
                cola.append(new_nodo)

        elif op == "izquierda" and izquierda != -1 and izquierda != 1:  #
            if (nodo_padre.operador == "derecha" and (nodo_padre.nave != nave_hijo) or # se verifica que si se puede devolver
                (nodo_padre.operador != "derecha" )): # O verifica que no haya un muro en la siguiente casilla y se verifica que no se regrese
                new_nodo = Nodo(matriz_copia, x, y-1, nodo_padre, "izquierda", aux_profundidad, 0, nave_hijo, nuevo_combustible, nodo_padre.cantidad_item)
                cola.append(new_nodo)

        elif op == "derecha" and derecha != -1 and derecha != 1: 
            if (nodo_padre.operador == "izquierda" and (nodo_padre.nave != nave_hijo) or # se verifica que si se puede devolver
                (nodo_padre.operador != "izquierda" )): # O verifica que no haya un muro en la siguiente casilla y se verifica que no se regrese
                new_nodo = Nodo(matriz_copia, x, y+1, nodo_padre, "derecha", aux_profundidad, 0, nave_hijo, nuevo_combustible, nodo_padre.cantidad_item)
                cola.append(new_nodo)