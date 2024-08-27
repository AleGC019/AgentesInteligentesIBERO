# Ejemplo de uso
# initial_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
# goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]

import time
import psutil
from collections import deque
from heapq import heappush, heappop


def print_matrix(state):
    """Imprime la matriz en formato de 3x3."""
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()  # Línea en blanco para mayor claridad


# Implementación del algoritmo BFS
def bfs(initial, goal):
    """Resuelve el puzzle utilizando BFS."""
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
def manhattan_distance(state, goal):
    """Calcula la suma de distancias de Manhattan para cada bloque."""
    distance = 0
    for i in range(1, 9):
        x1, y1 = divmod(state.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


def a_star(initial, goal):
    """Resuelve el puzzle utilizando A*."""
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Abajo, Arriba, Derecha, Izquierda
    open_set = []
    heappush(open_set, (0, initial, []))
    visited = set()

    while open_set:
        cost, state, path = heappop(open_set)

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
                    new_cost = cost + 1 + manhattan_distance(new_state, goal)
                    heappush(open_set, (new_cost, new_state, path + [new_state]))

    return None  # No se encontró solución


# Ejemplo de uso
initial_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]

# Imprimir el estado inicial
print("Estado inicial:")
print_matrix(initial_state)

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
solution_a_star = a_star(initial_state, goal_state)
end_time = time.perf_counter()
end_memory = process.memory_info().rss / 1024  # Memoria al final en KB
a_star_time = end_time - start_time
a_star_memory_usage = end_memory - start_memory

# Imprimir el estado final y resultados
print("Estado final (objetivo):")
print_matrix(goal_state)

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