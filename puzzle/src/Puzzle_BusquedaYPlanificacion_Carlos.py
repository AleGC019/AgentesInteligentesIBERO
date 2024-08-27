import time  # Importamos la librería 'time' para medir el tiempo de ejecución del algoritmo.

# Estado inicial del puzzle de 8 dígitos.
# El 0 representa el espacio vacío que puede moverse.
initial_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

# Estado objetivo al que queremos llegar.
goal_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]


def manhattan_distance(state):
    """
    Calcula la distancia de Manhattan entre el estado actual y el estado objetivo.

    La distancia de Manhattan es la suma de las distancias absolutas entre las posiciones
    actuales y las posiciones objetivo de cada número.

    :param state: Estado actual del puzzle representado como una lista de listas.
    :return: Distancia de Manhattan total.
    """
    distance = 0
    for i in range(3):  # Recorremos las filas del estado.
        for j in range(3):  # Recorremos las columnas del estado.
            value = state[i][j]
            if value != 0:  # El espacio vacío (0) no se cuenta en la distancia.
                # Calculamos la posición objetivo del valor actual.
                goal_x, goal_y = divmod(value - 1, 3)
                # Calculamos la distancia de Manhattan para el valor actual.
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def get_neighbors(state):
    """
    Genera todos los posibles estados vecinos del estado actual moviendo el espacio vacío.

    :param state: Estado actual del puzzle representado como una lista de listas.
    :return: Lista de estados vecinos generados.
    """
    neighbors = []
    x, y = find_blank(state)  # Encuentra la posición del espacio vacío en el estado.
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Direcciones posibles: arriba, abajo, izquierda, derecha.

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:  # Verifica que la nueva posición esté dentro de los límites.
            new_state = [row[:] for row in state]  # Crea una copia del estado actual.
            # Intercambia el espacio vacío con el valor en la nueva posición.
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)  # Añade el nuevo estado a la lista de vecinos.

    return neighbors


def find_blank(state):
    """
    Encuentra la posición del espacio vacío (0) en el estado del puzzle.

    :param state: Estado actual del puzzle representado como una lista de listas.
    :return: Tupla con las coordenadas (fila, columna) del espacio vacío.
    """
    for i in range(3):  # Recorremos las filas del estado.
        for j in range(3):  # Recorremos las columnas del estado.
            if state[i][j] == 0:  # Verifica si el valor en la posición actual es el espacio vacío.
                return i, j  # Retorna las coordenadas del espacio vacío.


def a_star(initial_state):
    """
    Ejecuta el algoritmo A* para encontrar la solución del puzzle de 8 dígitos.

    :param initial_state: Estado inicial del puzzle representado como una lista de listas.
    :return: Tupla con el camino a la solución (si se encuentra), el número de nodos explorados,
            el factor de ramificación máximo y la profundidad de la solución.
    """
    open_set = [(0, initial_state)]  # Cola de prioridad con el estado inicial. Se usa una tupla (costo total, estado).
    came_from = {}  # Diccionario para rastrear el camino recorrido.
    g_score = {str(initial_state): 0}  # Diccionario que almacena el costo de llegar a cada estado.
    nodes_explored = 0  # Contador de nodos explorados.
    max_branching_factor = 0  # Máximo número de vecinos generados en cualquier nodo.
    total_neighbors_count = 0  # Total de vecinos generados durante la ejecución.

    while open_set:
        _, current = open_set.pop(0)  # Extrae el estado con el menor costo total de la cola de prioridad.
        nodes_explored += 1  # Incrementa el contador de nodos explorados.

        # Obtiene todos los vecinos del estado actual.
        neighbors = get_neighbors(current)
        total_neighbors_count += len(neighbors)  # Suma la cantidad de vecinos generados.
        max_branching_factor = max(max_branching_factor, len(neighbors))  # Actualiza el factor de ramificación máximo.

        if current == goal_state:  # Verifica si hemos llegado al estado objetivo.
            return reconstruct_path(came_from, current), nodes_explored, max_branching_factor, g_score[str(current)]

        for neighbor in neighbors:
            tentative_g_score = g_score[str(current)] + 1  # Calcula el costo temporal para llegar al vecino.

            # Si el vecino no ha sido visitado o se ha encontrado un camino mejor, actualiza la información.
            if str(neighbor) not in g_score or tentative_g_score < g_score[str(neighbor)]:
                came_from[str(neighbor)] = current  # Registra de dónde proviene el vecino.
                g_score[str(neighbor)] = tentative_g_score  # Actualiza el costo de llegar al vecino.
                open_set.append((tentative_g_score + manhattan_distance(neighbor),
                                 neighbor))  # Añade el vecino a la cola de prioridad.
                open_set.sort(key=lambda x: x[0])  # Ordena la cola de prioridad por el costo total.

    return None, nodes_explored, max_branching_factor, None  # Retorna None si no se encuentra solución.


def reconstruct_path(came_from, current):
    """
    Reconstruye el camino desde el estado final hasta el estado inicial.

    :param came_from: Diccionario que rastrea el camino recorrido.
    :param current: Estado actual que se está reconstruyendo.
    :return: Lista de estados que representa el camino desde el estado inicial al final.
    """
    path = [current]  # Inicia el camino con el estado final.
    while str(current) in came_from:
        current = came_from[str(current)]  # Regresa al estado anterior en el camino.
        path.insert(0, current)  # Inserta el estado en la posición inicial del camino.
    return path


# Medir el tiempo de ejecución.
start_time = time.time()
path, nodes_explored, max_branching_factor, solution_depth = a_star(initial_state)
end_time = time.time()
execution_time = end_time - start_time  # Calcula el tiempo total de ejecución.

if path:
    print("Solución encontrada:")
    for step in path:
        for row in step:
            print(row)  # Imprime cada fila del estado del puzzle en el camino.
        print()
else:
    print("No se encontró una solución.")

print(f"Tiempo de ejecución: {execution_time:.4f} segundos")  # Muestra el tiempo total de ejecución.
print(f"Número de nodos explorados: {nodes_explored}")  # Muestra el número total de nodos explorados.

# Imprimir factor de ramificación y profundidad de la solución.
print(f"Factor de ramificación máximo observado: {max_branching_factor}")
print(f"Profundidad de la solución: {solution_depth}")

# Complejidad del algoritmo
print("Complejidad del algoritmo A* para el puzzle de 8 dígitos:")
print(
    " - Complejidad en Tiempo: O(b^d * log n)")  # Tiempo de ejecución en función del factor de ramificación (b) y la profundidad (d).
print(
    " - Complejidad en Espacio: O(b^d)")  # Espacio necesario en función del factor de ramificación (b) y la profundidad (d).
print("Donde:")
print("  - b = Factor de ramificación (hasta 4 vecinos por nodo)")  # Número máximo de vecinos que un nodo puede tener.
print("  - d = Profundidad de la solución")  # Número de movimientos necesarios para alcanzar el objetivo.
print("  - n = Número total de nodos explorados")  # Número de nodos explorados durante la búsqueda.
