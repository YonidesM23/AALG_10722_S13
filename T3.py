laberinto = [
    [1,  1,  1,  1,  99, 1,  1,  1,  0],   # Inicio (0,8)
    [1,  99, 99, 1,  99, 1,  99,  1,  99],
    [1,  1,  99, 1,  1,  1,  99,  1,  99],
    [99, 1,  99, 1,  99, 99, 99, 1,  99],
    [1,  1,  99, -1, 1,  1,  1,  3,  99],
    [-2, 99, 99, 1,  99, 99, 99, 1,  1],
    [1,  99, 1, -1, 1,  1,  1,  1,  99],
    [1,  99, 99, 99, 99, 2,  99, 1,  99],
    [0,  1,  3,  1,  1,  1,  99, 1,  1]   # Final (8,0)
]

inicio = (0, 8)
final  = (8, 0)


movs = [(0,-1), (1,0), (-1,0), (0,1)]

# Matriz para marcar el camino recorrido
camino = [["-" for _ in range(9)] for _ in range(9)]

ENERGIA_MAX = 18


# -----------------------------------------------
# FUNCIÓN DE BACKTRACKING
# -----------------------------------------------
def resolver(x, y, energia):

    if (x, y) == final:
        camino[x][y] = "X"
        print(f"LLEGÓ A LA META en {x},{y} con energía {energia}")
        return True


    camino[x][y] = "X"


    for dx, dy in movs:
        nx = x + dx
        ny = y + dy


        if nx < 0 or nx >= 9 or ny < 0 or ny >= 9:
            continue


        if laberinto[nx][ny] == 99:
            continue


        if camino[nx][ny] == "X":
            continue

        # Energía antes del movimiento
        energia_antes = energia
        valor = laberinto[nx][ny]
        nueva_energia = energia


        if valor > 0:
            nueva_energia -= valor
        elif valor < 0:
            nueva_energia += abs(valor)
            if nueva_energia > ENERGIA_MAX:
                nueva_energia = ENERGIA_MAX

        # Si la energía es insuficiente, no avanzar
        if nueva_energia < 0:
            continue

        # Mostrar información de energía
        print(f"Moviendo a ({nx},{ny})  Valor:{valor}  Energía:{energia_antes} → {nueva_energia}")

        if resolver(nx, ny, nueva_energia):
            return True

    camino[x][y] = "-"
    return False


# -----------------------------------------------
# PROGRAMA PRINCIPAL
# -----------------------------------------------

print("LABERINTO ORIGINAL:")
for fila in laberinto:
    print(fila)

print("\nBuscando camino usando Backtracking...\n")

exito = resolver(inicio[0], inicio[1], ENERGIA_MAX)

if exito:
    print("\n¡Se logró encontrar un camino hacia la salida!\n")
else:
    print("\nNo se logró encontrar un camino hacia la salida con la energía disponible.\n")

print("MATRIZ DEL CAMINO (X indica el camino tomado):\n")
for fila in camino:
    print(fila)