from collections import deque

# Función para imprimir el tablero
def print_tablero(tablero):
    for fila in tablero:
        print(" ".join(map(str, fila)))

# Función para encontrar la posición del número 7 en el tablero
def encontrar_posicion(tablero, objetivo):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == objetivo:
                return (i, j)

# Función para verificar si una posición está dentro del tablero
def es_valida(x, y):
    return 0 <= x < 3 and 0 <= y < 3

# Función para realizar movimientos y encontrar la solución
def resolver_puzzle(tablero, objetivo):
    inicio = encontrar_posicion(tablero, objetivo)
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Derecha, Izquierda, Abajo, Arriba
    visitados = set()
    cola = deque([(inicio, 0, [])])

    while cola:
        (x, y), costo, camino = cola.popleft()
        if tablero[x][y] == objetivo:
            print("Solución encontrada:")
            print("Camino tomado:")
            for c in camino:
                print(c)
            print("Costo total de movimientos:", costo)
            print("Coordenadas finales:", (x, y))
            return

        for dx, dy in movimientos:
            nueva_x, nueva_y = x + dx, y + dy
            if es_valida(nueva_x, nueva_y) and (nueva_x, nueva_y) not in visitados:
                nueva_camino = camino + [(nueva_x, nueva_y)]
                cola.append(((nueva_x, nueva_y), costo + 1, nueva_camino))
                visitados.add((nueva_x, nueva_y))

    print("No se encontró solución")

# Tablero de inicio
tablero_inicio = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor objetivo
objetivo = 9

print("Tablero de inicio:")
print_tablero(tablero_inicio)
print("Valor objetivo:", objetivo)
print("Resolviendo el puzzle...")
resolver_puzzle(tablero_inicio, objetivo)
