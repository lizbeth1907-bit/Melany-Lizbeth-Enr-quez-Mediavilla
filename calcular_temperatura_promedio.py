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