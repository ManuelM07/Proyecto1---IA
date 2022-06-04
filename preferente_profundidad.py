from nodo import Nodo, operadores
import numpy as np

cola = []
nodos_expandidos = 0

# funcion que implementa el algoritmo de búsqueda preferente por profundidad.
def preferente_profundidad(matriz, x, y):
    global cola, nodos_expandidos

        
    nodo_raiz = Nodo(matriz, x, y, None, None, 0, 0, False, 0, 0, matriz)
    cola.append(nodo_raiz)

    while True: 
        if cola == []:
            return "Falla"
        cabeza = cola[0]
        nodos_expandidos += 1
        cola = cola[1:]
        cabeza.actualizar_estado_casilla()
        if cabeza.es_meta():
            print("nodos expandidos: ", nodos_expandidos)
            print("profundidad: ", cabeza.profundidad)
            print("costo:", cabeza.costo)
            return cabeza.encontrar_camino() 
        crear_hijos(cabeza)            


def crear_hijos(nodo_padre):

    global cola
    nave_hijo = nodo_padre.validar_nave()
    nuevo_combustible = nodo_padre.combustible-1 if nave_hijo else 0

    matriz_copia = nodo_padre.matriz.copy()
    x = nodo_padre.x
    y = nodo_padre.y

    aux_profundidad = nodo_padre.profundidad + 1 

    matriz_copia = restringir_camino(matriz_copia, x, y).copy()
    matriz_copia = validar_cambio_matriz(nodo_padre, matriz_copia, x, y).copy() 
    derecha = nodo_padre.estado["derecha"]
    izquierda = nodo_padre.estado["izquierda"]
    abajo = nodo_padre.estado["abajo"]
    arriba = nodo_padre.estado["arriba"]

    for i in range(len(operadores)-1, -1, -1):


        if (operadores[i] == "arriba" and arriba > -1 and arriba != 1): #verifica que se puede mover (no sale de la matriz y no hay un muro).
            if (nodo_padre.operador == "abajo" and (nodo_padre.nave != nodo_padre.nodo_padre.nave or nodo_padre.item_encontrado) or # verifica que se puede devolver
                (nodo_padre.operador != "abajo" )): # O verifica que no se regrese
                 
                new_nodo = Nodo(matriz_copia, x-1, y, nodo_padre, "arriba", aux_profundidad, nodo_padre.costo, nave_hijo, nuevo_combustible, nodo_padre.cantidad_item, nodo_padre.matriz_aux)
                cola.insert(0, new_nodo)

        elif (operadores[i] == "abajo" and abajo > -1 and abajo != 1): #verifica que se puede mover (no sale de la matriz y no hay un muro).
            if (nodo_padre.operador == "arriba" and (nodo_padre.nave != nodo_padre.nodo_padre.nave or nodo_padre.item_encontrado) or # se verifica que se puede devolver
                (nodo_padre.operador != "arriba" )): # O verifica que no se regrese
                
                new_nodo = Nodo(matriz_copia, x+1, y, nodo_padre, "abajo", aux_profundidad, nodo_padre.costo, nave_hijo, nuevo_combustible, nodo_padre.cantidad_item, nodo_padre.matriz_aux)
                cola.insert(0, new_nodo)

        elif (operadores[i] == "izquierda" and izquierda > -1 and izquierda != 1): #verifica que se puede mover (no sale de la matriz y no hay un muro). 
            if (nodo_padre.operador == "derecha" and (nodo_padre.nave != nodo_padre.nodo_padre.nave or nodo_padre.item_encontrado) or # se verifica que se puede devolver
                (nodo_padre.operador != "derecha" )): # O verifica que no se regrese
                
                new_nodo = Nodo(matriz_copia, x, y-1, nodo_padre, "izquierda", aux_profundidad, nodo_padre.costo, nave_hijo, nuevo_combustible, nodo_padre.cantidad_item, nodo_padre.matriz_aux)
                cola.insert(0, new_nodo)

        elif (operadores[i] == "derecha" and derecha > -1 and derecha != 1): #verifica que se puede mover (no sale de la matriz y no hay un muro).
            if (nodo_padre.operador == "izquierda" and (nodo_padre.nave != nodo_padre.nodo_padre.nave or nodo_padre.item_encontrado) or # se verifica que se puede devolver
                (nodo_padre.operador != "izquierda" )): # O verifica que no se regrese
                
                new_nodo = Nodo(matriz_copia, x, y+1, nodo_padre, "derecha", aux_profundidad, nodo_padre.costo, nave_hijo, nuevo_combustible, nodo_padre.cantidad_item, nodo_padre.matriz_aux)
                cola.insert(0, new_nodo)


def validar_cambio_matriz(nodo_padre, matriz, x, y):
    """ Se valida si es necesario hacer un cambio a la matriz,
        dependiendo si se encontró con una nave o un item,
        si uno de estos casos se cumple se cambia a la matriz inicial, 
        pero quitando el item o la nave que se encuentre en la posición inicial. """

    try:
        print(nodo_padre.item_encontrado)
        if (nodo_padre.combustible == 20) or (nodo_padre.combustible == 10 and nodo_padre.nodo_padre.combustible != 11) or nodo_padre.item_encontrado:
            nodo_padre.matriz_aux[x][y] = 0
            nodo_padre.matriz = np.array(nodo_padre.matriz_aux)
            nodo_padre.estado = nodo_padre.validar_direcciones(x, y)

            return nodo_padre.matriz_aux
    except AttributeError:
        return matriz
    else: 
        return matriz


def restringir_camino(matriz, x, y):
    """ Restringe el camino por donde pasa, para evitar entrar en un ciclo. """
    if matriz[x][y] == 6 or matriz[x][y] == -6:
        matriz[x][y] = -6
    elif matriz[x][y] == 2 or matriz[x][y] == -2:
        matriz[x][y] = -2
    else:
        matriz[x][y] = -1
    return matriz 