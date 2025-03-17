def bubble_sort(fila):
    """Ordena una lista usando el algoritmo Bubble Sort"""
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j] 


# Crear una matriz 3x3 con números
matriz = [
    [8, 3, 5],
    [1, 9, 4],
    [6, 2, 7]
]

fila_a_ordenar = 1  
fila = matriz[fila_a_ordenar].copy() 

bubble_sort(fila)  
matriz[fila_a_ordenar] = fila  

# Mostrar la matriz actualizada
print("Matriz con la fila ordenada:")
for fila in matriz:
    print(fila)
