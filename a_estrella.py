﻿from nodo import Nodo, operadores
import queue

cola_prioridad = queue.PriorityQueue() # importante tener cuidado con el límite 
nodos_expandidos = 0
contador = 0
pos_item1 = {}
pos_item2 = {}
buscar_item1 = True
buscar_item2 = True 
distancia_items = 0  

# funcion que implementa el algoritmo de búsqueda preferente por amplitud.
def a_estrella(matriz, x, y, posItem1, posItem2):
    
    global cola_prioridad, nodos_expandidos, pos_item1, pos_item2, distancia_items

    pos_item1 = posItem1
    pos_item2 = posItem2

    nodo_raiz = Nodo(matriz, x, y, None, None, 0, 0, False, 0, 0)
    cola_prioridad.put(nodo_raiz)

    distancia_items = manhattan(pos_item1["x"], pos_item1["y"], pos_item2["x"], pos_item2["y"])

    while True: 
        if cola_prioridad.empty():
            print("No se ha encontrado el camino.")
            exit(-1)
            return "Falla"
        cabeza = cola_prioridad.get()
        nodos_expandidos += 1
        
        if cabeza.es_meta():
            print("nodos expandidos: ", nodos_expandidos)
            print("profundidad: ", cabeza.profundidad)
            print("costo:", cabeza.costo)
            return cabeza.encontrar_camino() 
        crear_hijos(cabeza)            

# función que calcula la distancia de manhattan de un nodo con respecto a un ítem.
def manhattan(x1, y1, x2, y2): # nodo, pos_item
    # resultado = abs(nodo.x - pos_item['posx']) + abs(nodo.y - pos_item['posy'])
    resultado = abs(x2 - x1) + abs(y2 - y1)
    return resultado

def calcular_heuristica(nodo):
    global buscar_item1, buscar_item2, distancia_items
    #  min(mh(agente, item1) + mh(item1, item2), mh(agente, item2) + mh(item1, item2))

    
    if buscar_item2 and not buscar_item1: # solo busca el item2 (ya encontró el 1).
        manhattan_item = manhattan(nodo.x, nodo.y, pos_item2["x"], pos_item2['y'])
        distancia_total = manhattan_item
    elif buscar_item1 and not buscar_item2: # solo busca el item1 (ya encontró el 2).
        manhattan_item = manhattan(nodo.x, nodo.y, pos_item1["x"], pos_item1['y'])
        distancia_total = manhattan_item
    elif buscar_item1 and buscar_item2:
        manhattan_item1 = manhattan(nodo.x, nodo.y, pos_item1["x"], pos_item1['y'])
        manhattan_item2 = manhattan(nodo.x, nodo.y, pos_item2["x"], pos_item2['y'])
        if manhattan_item1 == 0:
            buscar_item1 = False
            print("encontró el item1")
        elif manhattan_item2 == 0:
            print("encontró el item2")
            buscar_item2 = False

        distancia_total = min((manhattan_item1 + distancia_items), (manhattan_item2 + distancia_items))  # manhattan_item1 + manhattan_item2 # no ha encontrado ningún ítem
    return distancia_total

def crear_hijos(nodo_padre):
    global contador 
    global cola_prioridad

    contador += 1 

    nave_hijo = nodo_padre.validar_nave()
    nuevo_combustible = nodo_padre.combustible-1 if nave_hijo else 0

    matriz_copia = nodo_padre.matriz.copy()
    x = nodo_padre.x
    y = nodo_padre.y

    derecha = nodo_padre.estado["derecha"] 
    izquierda = nodo_padre.estado["izquierda"] 
    abajo = nodo_padre.estado["abajo"] 
    arriba = nodo_padre.estado["arriba"] 

    aux_profundidad = nodo_padre.profundidad + 1 
    costo_padre = nodo_padre.costo

    for op in operadores:

        if (op == "arriba" and arriba != -1 and arriba != 1): #verifica que se puede mover (no sale de la matriz y no hay un muro).
            if ((nodo_padre.operador == "abajo" and (nodo_padre.nodo_padre.nave != nave_hijo or nodo_padre.item_encontrado)) or # verifica que se puede devolver
                (nodo_padre.operador != "abajo" )): # O verifica que no se regrese
                
                new_nodo = Nodo(matriz_copia, x-1, y, nodo_padre, "arriba", aux_profundidad, costo_padre, nave_hijo, nuevo_combustible, nodo_padre.cantidad_item)
                new_nodo.actualizar_estado_casilla()
                new_nodo.heuristica = calcular_heuristica(new_nodo)
                #new_nodo.costo += calcular_costo(new_nodo.matriz[new_nodo.x][new_nodo.y], new_nodo.nave)
                cola_prioridad.put(new_nodo)

        elif (op == "abajo" and abajo != -1 and abajo != 1): #verifica que se puede mover (no sale de la matriz y no hay un muro).
            if ((nodo_padre.operador == "arriba" and (nodo_padre.nodo_padre.nave != nave_hijo or nodo_padre.item_encontrado)) or # se verifica que se puede devolver
                (nodo_padre.operador != "arriba" )): # O verifica que no se regrese
                
                new_nodo = Nodo(matriz_copia, x+1, y, nodo_padre, "abajo", aux_profundidad, costo_padre, nave_hijo, nuevo_combustible, nodo_padre.cantidad_item)
                new_nodo.actualizar_estado_casilla()
                new_nodo.heuristica = calcular_heuristica(new_nodo)
                #new_nodo.costo += calcular_costo(new_nodo.matriz[new_nodo.x][new_nodo.y], new_nodo.nave)
                cola_prioridad.put(new_nodo)

        elif (op == "izquierda" and izquierda != -1 and izquierda != 1): #verifica que se puede mover (no sale de la matriz y no hay un muro). 
            if ((nodo_padre.operador == "derecha" and (nodo_padre.nodo_padre.nave != nave_hijo or nodo_padre.item_encontrado)) or # se verifica que se puede devolver
                (nodo_padre.operador != "derecha" )): # O verifica que no se regrese
                
                new_nodo = Nodo(matriz_copia, x, y-1, nodo_padre, "izquierda", aux_profundidad, costo_padre, nave_hijo, nuevo_combustible, nodo_padre.cantidad_item)
                new_nodo.actualizar_estado_casilla()
                new_nodo.heuristica = calcular_heuristica(new_nodo)
                #new_nodo.costo += calcular_costo(new_nodo.matriz[new_nodo.x][new_nodo.y], new_nodo.nave)
                cola_prioridad.put(new_nodo)

        elif (op == "derecha" and derecha != -1 and derecha != 1): #verifica que se puede mover (no sale de la matriz y no hay un muro).
            if ((nodo_padre.operador == "izquierda" and (nodo_padre.nodo_padre.nave != nave_hijo or nodo_padre.item_encontrado)) or # se verifica que se puede devolver
                (nodo_padre.operador != "izquierda" )): # O verifica que no se regrese
               
                new_nodo = Nodo(matriz_copia, x, y+1, nodo_padre, "derecha", aux_profundidad, costo_padre, nave_hijo, nuevo_combustible, nodo_padre.cantidad_item)
                new_nodo.actualizar_estado_casilla()
                new_nodo.heuristica = calcular_heuristica(new_nodo)
                #new_nodo.costo += calcular_costo(new_nodo.matriz[new_nodo.x][new_nodo.y], new_nodo.nave)
                cola_prioridad.put(new_nodo)