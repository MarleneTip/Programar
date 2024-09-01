# Definimos la matriz bidimensional 3x3 con valores numéricos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor_a_buscar):
    # Recorremos las filas de la matriz
    for i in range(len(matriz)):
        # Recorremos las columnas de la matriz
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_a_buscar:
                return f"Valor {valor_a_buscar} encontrado en la posición ({i}, {j})"
    return f"Valor {valor_a_buscar} no encontrado en la matriz"

# Definimos el valor a buscar
valor = 5

# Llamamos a la función de búsqueda
resultado = buscar_valor(matriz, valor)

# Imprimimos el resultado
print(resultado)
