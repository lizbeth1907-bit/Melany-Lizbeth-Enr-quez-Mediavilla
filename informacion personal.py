# Crear un Diccionario
informacion_personal = {
    'nombre': 'Carlos López',
    'edad': 25,
    'ciudad': 'Puyo',
    'profesion': 'Estudiante'
}

# Acceder y Modificar Valores
informacion_personal['ciudad'] = 'Tena'  # Modificar la ciudad
informacion_personal['profesion'] = 'Ingeniero'  # Modificar la profesión

# Verificar Existencia de Claves
if 'telefono' not in informacion_personal:
    informacion_personal['telefono'] = '0987654321'  # Agregar teléfono ficticio

# Eliminar una Clave
del informacion_personal['edad']  # Eliminar la clave "edad"

# Imprimir el Diccionario Final
print(informacion_personal)
