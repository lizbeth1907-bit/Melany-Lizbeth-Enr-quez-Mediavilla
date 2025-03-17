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
   def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad.
    
    :param datos_temperaturas: Lista de listas con temperaturas de múltiples ciudades en varias semanas.
    :return: Lista con la temperatura promedio de cada ciudad.
    """
    promedios = []
    for ciudad in datos_temperaturas:
        promedio_ciudad = sum(ciudad) / len(ciudad)  
        promedios.append(promedio_ciudad)
    return promedios


# Datos de temperaturas (3 ciudades, 4 semanas)
datos_temperaturas = [
    [22, 24, 19, 23],  # Ciudad 1
    [30, 29, 31, 32],  # Ciudad 2
    [18, 20, 17, 19]   # Ciudad 3
]

# Calcular temperaturas promedio
promedios = calcular_temperatura_promedio(datos_temperaturas)

# Mostrar resultados
for i, promedio in enumerate(promedios, 1):
    print(f"Temperatura promedio de la Ciudad {i}: {promedio:.2f}°C")