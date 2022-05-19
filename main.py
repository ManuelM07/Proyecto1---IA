"""matriz = [
          [0, 0, 0], # toma la nave 
          [4, 0, 0], # consumido 2, 1, 0
          [1, 0, 0]] # si el padre tiene nave -> 
nodo_padre = None

x = 0
y = 0
cantidad_item = 0
nodos_expandidos = 5
profundidad = 0
total_items = 6
tiene_nave = False"""

from numpy import matrix
from preferencia_amplitud import preferencia_amplitud


nombre_lectura = "mundo"
n = 10
x0 = 0 
y0 = 0

def input():
    global x0, y0

    with open(f"{nombre_lectura}.txt", "r") as f:
        content = f.read().split('\n')
        mundo = []
        for i in range(n):
            fila = list(map(lambda x: int(x), content[i].split(" ")))
            mundo.append(fila)
            try: 
                y0 = fila.index(2)
                x0 = i
            except ValueError:
                pass

        return mundo

matrix_l = input()



def mostrar_mundo(matrix_):
    for fila in matrix_l:
        print(fila)




mostrar_mundo(matrix_l)
#print(x0, y0)
resultado = preferencia_amplitud(matrix_l, x0, y0)
print(resultado)

def costo(peso, nave) -> int:
    if peso == 6 and not nave:
        return 4
    else:
        return 1


