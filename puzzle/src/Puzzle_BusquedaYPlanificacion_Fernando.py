#############################################
#   UNIVERSIDAD IBEROAMERICANA DE PUEBLA    #
#   Tema 3 - Busqueda y planificacion       #
#   Eguizabal Medrano, Fernando Andres      #
#############################################

# Importacion de librerias y utilidades
import time
import psutil
from collections import deque
from tabulate import tabulate
from heapq import heappush, heappop

def print_matrix(state, jump):
    
    for i in range(0, len(state), jump):
        print(state[i:i + jump]) # Imprimir el estado del puzzle
    
    print()  # Salto de línea

# Implementación del algoritmo BFS
def bfs(initial, goal):
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Abajo, Arriba, Derecha, Izquierda
    queue = deque([(initial, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        visited.add(tuple(state))

        zero_index = state.index(0)
        x, y = divmod(zero_index, 3)

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = state[:]
                swap_index = nx * 3 + ny
                new_state[zero_index], new_state[swap_index] = new_state[swap_index], new_state[zero_index]

                if tuple(new_state) not in visited:
                    queue.append((new_state, path + [new_state]))

    return None  # No se encontró solución

# Implementación del algoritmo A*
def manhattan_distance(state, goal, elements):

    # Calcula la suma de distancias de Manhattan para cada bloque.
    distance = 0

    for i in range(1, elements):

        # Encuentra las coordenadas (x, y) de cada bloque en el estado actual y en el objetivo.
        x1, y1 = divmod(state.index(i), 3)

        # Encuentra las coordenadas (x, y) de cada bloque en el estado objetivo.
        x2, y2 = divmod(goal.index(i), 3)

        # Calcula la distancia de Manhattan para cada bloque.
        distance += abs(x1 - x2) + abs(y1 - y2)

    return distance

# Implementacion del algoritmo A*
def a_star(initial, goal, limit):

    # Se asume inicialmente que los datos pasados por medio de initial y goal, además de tener la
    # misma dimensión, son arreglos cuadrados.

    # Arreglo de movimientos
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Abajo, Arriba, Derecha, Izquierda
    
    # Cola de prioridad
    open_set = []

    # Agregar el estado inicial a la cola de prioridad
    heappush(open_set, (0, initial, []))

    # Conjunto de estados visitados
    visited = set()

    # Mientras la cola de prioridad no esté vacía
    while open_set:

        # Extraer el estado con menor costo
        cost, state, path = heappop(open_set)

        # Si el estado es igual al objetivo, regresar el camino
        if state == goal:
            return path

        # Si no, agregar el estado a los visitados
        visited.add(tuple(state))

        # Encontrar la posición del cero, o sea, del espacio vacío
        zero_index = state.index(0)

        # Calcular las coordenadas (x, y) del espacio vacío a través de la tupla (divmod) 
        # que devuelve el cociente (fila) y el residuo (columna) de la división
        x, y = divmod(zero_index, limit)

        # Para las posibles variaciones de x e y dentro de los movimientos...
        for dx, dy in moves:

            # Calcular las posibles nuevas coordenadas
            nx, ny = x + dx, y + dy

            # Si las coordenadas están dentro del rango...
            if 0 <= nx < limit and 0 <= ny < limit:
                # Copiar el estado actual
                new_state = state[:]    

                # Calcular el índice del nuevo estado
                swap_index = nx * limit + ny    

                # Intercambiar los valores del espacio vacío y el nuevo estado
                new_state[zero_index], new_state[swap_index] = new_state[swap_index], new_state[zero_index]   

                # Si el nuevo estado no ha sido visitado...
                if tuple(new_state) not in visited:

                    # Calcular el nuevo costo y agregarlo a la cola de prioridad
                    new_cost = cost + 1 + manhattan_distance(new_state, goal, len(state))

                    # Agregar el nuevo estado a la cola de prioridad
                    heappush(open_set, (new_cost, new_state, path + [new_state]))

    # Si no se encontró solución, regresar None
    return None  


# Ejemplo de uso
initial_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
# [2, 8, 3]
# [1, 6, 4]
# [7, 0, 5]

goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
# [1, 2, 3]
# [8, 0, 4]
# [7, 6, 5]

# Imprimir el estado inicial
print("Estado inicial:")
print_matrix(initial_state, 3)

# Monitorear tiempo y memoria para BFS
process = psutil.Process()
start_memory = process.memory_info().rss / 1024  # Memoria al inicio en KB
start_time = time.perf_counter()
solution_bfs = bfs(initial_state, goal_state)
end_time = time.perf_counter()
end_memory = process.memory_info().rss / 1024  # Memoria al final en KB
bfs_time = end_time - start_time
bfs_memory_usage = end_memory - start_memory

# Monitorear tiempo y memoria para A*
process = psutil.Process()
start_memory = process.memory_info().rss / 1024  # Memoria al inicio en KB
start_time = time.perf_counter()
solution_a_star = a_star(initial_state, goal_state, 3)
end_time = time.perf_counter()
end_memory = process.memory_info().rss / 1024  # Memoria al final en KB
a_star_time = end_time - start_time
a_star_memory_usage = end_memory - start_memory

# Imprimir el estado final y resultados
print("Estado final (objetivo):")
print_matrix(goal_state, 3)

if solution_a_star:
    print("\nMovimientos para resolver el puzzle (A*):")
    for path in solution_a_star:
        print_matrix(path, 3)

print("\nResultados:")
print("Solución con BFS:")
if solution_bfs:
    print(f"Movimientos para resolver el puzzle (BFS): {len(solution_bfs)}")
else:
    print("No se encontró una solución con BFS.")
print(f"Tiempo de ejecución (BFS): {bfs_time:.6f} segundos")
print(f"Uso de memoria (BFS): {bfs_memory_usage:.2f} KB")

print("\nSolución con A*:")
if solution_a_star:
    print(f"Movimientos para resolver el puzzle (A*): {len(solution_a_star)}")
else:
    print("No se encontró una solución con A*.")
print(f"Tiempo de ejecución (A*): {a_star_time:.6f} segundos")
print(f"Uso de memoria (A*): {a_star_memory_usage:.2f} KB")

# Comparación de resultados dentro de una tabla
print("\nComparación de resultados:")

table = [
    ["Algoritmo", "Movimientos", "Tiempo de ejecución", "Uso de memoria"],
    ["BFS", len(solution_bfs) if solution_bfs else "No encontrado", f"{bfs_time:.6f} segundos", f"{bfs_memory_usage:.2f} KB"],
    ["A*", len(solution_a_star) if solution_a_star else "No encontrado", f"{a_star_time:.6f} segundos", f"{a_star_memory_usage:.2f} KB"]
]

print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))

# Conclusion
print("\nConclusión:")
print("El algoritmo A* es más eficiente que BFS en términos de tiempo y memoria.")