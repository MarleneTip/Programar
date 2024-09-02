# Definir la matriz 3x3
matriz = [
    [5, 8, 3],
    [6, 7, 1],
    [9, 4, 2]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):            # Recorre las filas
        for j in range(len(matriz[i])):     # Recorre las columnas
            if matriz[i][j] == valor_buscado:
                return (i, j)  # Retorna la posición (fila, columna) si se encuentra el valor
    return None  # Retorna None si no se encuentra el valor

# Valor a buscar
valor_buscado = 7

# Buscar el valor en la matriz
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
if posicion:
    print(f"El valor {valor_buscado} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
