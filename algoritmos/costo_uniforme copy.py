from algoritmos.nodo import Nodo, operadores
import queue

cola_prioridad = queue.PriorityQueue() # importante tener cuidado con el límite 
nodos_expandidos = 0
contador = 0

# funcion que implementa el algoritmo de búsqueda preferente por amplitud.
def costo_uniforme(matriz, x, y):
    
    global cola_prioridad, nodos_expandidos

    nodo_raiz = Nodo(matriz, x, y, None, None, 0, 0, False, 0, 0)
    cola_prioridad.put(nodo_raiz)

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

def crear_hijos(nodo_padre):
    global contador 
    global cola_prioridad

    contador += 1
    nave_hijo, nuevo_combustible = nodo_padre.validar_nave() 
    matriz_copia = nodo_padre.matriz.copy()
    aux_profundidad = nodo_padre.profundidad + 1 
    costo_padre = nodo_padre.costo
    x = nodo_padre.x
    y = nodo_padre.y

    valores_casillas = { "arriba": nodo_padre.estado["arriba"], 
                         "abajo": nodo_padre.estado["abajo"], 
                         "izquierda": nodo_padre.estado["izquierda"], 
                         "derecha": nodo_padre.estado["derecha"] }
    
    opuesto_de = { "arriba":"abajo", "abajo":"arriba", "izquierda":"derecha", "derecha":"izquierda" }

    nuevas_posiciones = { "arriba": [x-1, y], "abajo": [x+1, y], "izquierda": [x, y-1], "derecha": [x, y+1] }

    for op_actual in operadores: # ["derecha", "izquierda", etc]
        #contrario = anterior, ej: actual = arriba -> contrario = abajo
        casilla_siguiente = valores_casillas[op_actual] # guarda el valor de la casilla siguiente (en la que está cada hijo).
        
        if (casilla_siguiente != -1 and casilla_siguiente != 1):
            se_devuelve = nodo_padre.operador == opuesto_de[op_actual]
            if (nodo_padre.nodo_padre):
                tipo_nave_diferentes = nodo_padre.nodo_padre.nave != nave_hijo
            
            if ( (se_devuelve and ( tipo_nave_diferentes or nodo_padre.item_encontrado)) or not se_devuelve):

                nuevo_x = nuevas_posiciones[op_actual][0] # 0 -> x
                nuevo_y = nuevas_posiciones[op_actual][1] # 1 -> y

                new_nodo = Nodo(matriz_copia, nuevo_x, nuevo_y, nodo_padre, op_actual, aux_profundidad, costo_padre, nave_hijo, nuevo_combustible, nodo_padre.cantidad_item)
                new_nodo.actualizar_estado_casilla()
                cola_prioridad.put(new_nodo)