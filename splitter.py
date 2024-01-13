import os
import random
import shutil

# Ruta de la carpeta con las imágenes originales
carpeta_origen = 'train/blue/'

# Ruta de la carpeta donde se guardarán las imágenes de validación
carpeta_validacion = 'validation/blue/'

# Porcentaje de imágenes a copiar (en este caso, el 20%)
porcentaje = 0.20

# Obtén la lista de archivos en la carpeta de origen
archivos = os.listdir(carpeta_origen)

# Calcula la cantidad de imágenes a copiar
cantidad_a_copiar = int(len(archivos) * porcentaje)

# Elige aleatoriamente las imágenes a copiar
imagenes_a_copiar = random.sample(archivos, cantidad_a_copiar)

# Crea la carpeta de validación si no existe
if not os.path.exists(carpeta_validacion):
    os.makedirs(carpeta_validacion)

# Copia las imágenes seleccionadas a la carpeta de validación
for imagen in imagenes_a_copiar:
    origen = os.path.join(carpeta_origen, imagen)
    destino = os.path.join(carpeta_validacion, imagen)
    shutil.move(origen, destino)

print(f"{cantidad_a_copiar} imágenes han sido copiadas a la carpeta de validación.")
