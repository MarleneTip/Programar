# Definir la matriz 3x3
matriz = [
    [5, 8, 3],
    [6, 7, 1],
    [9, 4, 2]
]

# Función para ordenar una fila específica utilizando Bubble Sort
def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

# Función para ordenar una fila específica de la matriz
def ordenar_fila_matriz(matriz, fila_index):
    # Crear una copia de la matriz para mantener la original intacta
    matriz_ordenada = [row[:] for row in matriz]
    # Ordenar la fila específica
    bubble_sort_fila(matriz_ordenada[fila_index])
    return matriz_ordenada

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1) y mostrar la matriz resultante
fila_a_ordenar = 1
matriz_con_fila_ordenada = ordenar_fila_matriz(matriz, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz_con_fila_ordenada:
    print(fila)