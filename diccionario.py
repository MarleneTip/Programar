# crear el diccionario con datos ficticios

informacion_personal = {
    "nombre": "Ana Armas",
    "edad": 18,
    "ciudad": "Quito",
    "profesion": "Enfermero"
}

# Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Cuenca"

# Agregar nueva clave-valor para la "profesion"
informacion_personal["profesion"] = "Medico"

# Verificar existencia de la clave "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "01234567892"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)

