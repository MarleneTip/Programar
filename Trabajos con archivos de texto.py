# Creación de un nuevo archivo llamado my_notes.txt y escritura de notas personales
with open('my_notes.txt', 'w') as file:
    # Escribo tres líneas de notas
    file.write("Nota 1: Recuerda colocar alarma.\n")
    file.write("Nota 2: Recuerda las compras.\n")
    file.write("Nota 3: Recuerda tomar las pastillas.\n")

# Lectura del archivo my_notes.txt y mostrando el contenido línea por línea
with open('my_notes.txt', 'r') as file:
    # Leer cada línea y mostrar en consola
    for line in file:
        print(line.strip())  # Usamos strip() para eliminar saltos de línea adicionales
