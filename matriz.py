import numpy as np

# Crear una matriz de 3x3 con números aleatorios entre 1 y 100
matriz = np.random.randint(1, 101, (3, 3))

# Mostrar la matriz original
print("Matriz original:")
print(matriz)

# Elegir una fila para ordenar (por ejemplo, la fila 1 - segunda fila)
fila_a_ordenar = 1

# Ordenar la fila específica utilizando Bubble Sort
fila = matriz[fila_a_ordenar].copy()  # Copiar la fila para no modificar la original
fila.sort()  # Ordenar en orden ascendente

# Actualizar la matriz con la fila ordenada
matriz[fila_a_ordenar] = fila

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
print(matriz)