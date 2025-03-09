import random

# Definir dimensiones
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas

# Crear matriz 3D para almacenar temperaturas
temperaturas = [[[random.randint(10, 30) for _ in dias_semana] for _ in ciudades] for _ in range(semanas)]

# Mostrar la matriz con temperaturas generadas
for semana in range(semanas):
    print(f"\nSemana {semana + 1}:")
    for ciudad_idx, ciudad in enumerate(ciudades):
        print(f"  Ciudad: {ciudad}")
        for dia_idx, dia in enumerate(dias_semana):
            print(f"    {dia}: {temperaturas[semana][ciudad_idx][dia_idx]}°C")

# Calcular y mostrar el promedio de temperatura para cada ciudad en cada semana
for semana in range(semanas):
    print(f"\nPromedios de temperatura - Semana {semana + 1}:")
    for ciudad_idx, ciudad in enumerate(ciudades):
        promedio = sum(temperaturas[semana][ciudad_idx]) / len(dias_semana)
        print(f"  {ciudad}: {promedio:.2f}°C")