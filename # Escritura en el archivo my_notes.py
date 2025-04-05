# Escritura en el archivo my_notes.txt
archivo = open("my_notes.txt", "w")
archivo.write("Nota 1: Recordar estudiar Python todos los días.\n")
archivo.write("Nota 2: Practicar ejemplos de archivos de texto.\n")
archivo.write("Nota 3: Subir el código a GitHub.\n")
archivo.close()  # Cerrar el archivo después de escribir

# Lectura del archivo línea por línea
archivo = open("my_notes.txt", "r")
for linea in archivo:
    print(linea.strip())  # Mostrar cada línea sin saltos adicionales
archivo.close()  # Cerrar el archivo después de leer