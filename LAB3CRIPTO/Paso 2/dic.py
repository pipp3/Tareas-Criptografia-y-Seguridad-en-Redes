import re

# Nombre del archivo de entrada y salida
archivo_entrada = "rockyou.txt"
archivo_salida = "rockyou_mod.dic"

# Expresión regular para comprobar si una cadena comienza con una letra
patron_letra = re.compile(r"^[a-zA-Z]")

# Diccionario para almacenar las contraseñas modificadas
contrasenas_modificadas = []

# Abrir el archivo de entrada y procesar las contraseñas
with open(archivo_entrada, "rb") as f:
    for linea_bytes in f:
        linea = linea_bytes.decode("utf-8", errors="ignore").strip()
        if patron_letra.match(linea):
            # Reemplazar la primera letra por su versión en mayúscula y agregar un "0" al final
            nueva_contrasena = linea[0].upper() + linea[1:] + "0"
            contrasenas_modificadas.append(nueva_contrasena)

# Guardar las contraseñas modificadas en el nuevo archivo
with open(archivo_salida, "w") as f:
    for contrasena in contrasenas_modificadas:
        f.write(contrasena + "\n")

print(f"Se han modificado y guardado {len(contrasenas_modificadas)} contraseñas en {archivo_salida}")

