def buscar_valor(matriz, valor):
    """Busca un valor en la matriz y devuelve su posición si lo encuentra."""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición (fila, columna)
    return None

# Definir una matriz 3x3 con valores numéricos
matriz = [
    [4, 8, 15],
    [16, 23, 42],
    [10, 20, 30]
]

# Mostrar la matriz al usuario
print("Matriz:")
for fila in matriz:
    print(fila)

# Pedir al usuario que ingrese el valor a buscar
valor_buscado = int(input("Ingrese el valor a buscar en la matriz: "))

# Llamar a la función de búsqueda
resultado = buscar_valor(matriz, valor_buscado)

# Mostrar resultados
if resultado:
    print(f"El valor {valor_buscado} fue encontrado en la posición {resultado}.")
else:
    print(f"El valor {valor_buscado} no se encuentra en la matriz."