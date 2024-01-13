import os

# Ruta de la carpeta con las imágenes
carpeta = 'train/black/'

# Obtén la lista de archivos en la carpeta
archivos = os.listdir(carpeta)

# Inicializa una variable para llevar la cuenta del número
numero = 1

# Itera a través de los archivos y renómbralos
for archivo in archivos:
    # Verifica si el archivo es una imagen (puedes agregar más extensiones si es necesario)
    if archivo.endswith('.jpg') or archivo.endswith('.png'):
        # Crea el nuevo nombre del archivo con formato "1.jpg", "2.jpg", etc.
        nuevo_nombre = 'Black_' + str(numero) + '.jpg'
        
        # Ruta completa al archivo original y al nuevo nombre
        ruta_original = os.path.join(carpeta, archivo)
        nuevo_nombre_ruta = os.path.join(carpeta, nuevo_nombre)
        
        # Renombra el archivo
        os.rename(ruta_original, nuevo_nombre_ruta)
        
        # Incrementa el número para el siguiente archivo
        numero += 1

print("Archivos renombrados con éxito. ")
print("Total de archivos: ", numero - 1)
