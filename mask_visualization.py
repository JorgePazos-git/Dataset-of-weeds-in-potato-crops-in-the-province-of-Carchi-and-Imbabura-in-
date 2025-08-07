import os
import numpy as np
from PIL import Image

# Diccionario de colores para cada clase (excepto 0: background)
colores_clases = {
    1: [0, 0, 255],     # Cow-tongue
    2: [255, 165, 0],   # Dandelion
    3: [255, 255, 0],   # Kikuyo
    4: [128, 0, 128],   # Other
    5: [0, 128, 0],     # Potato
}

def convertir_mascara_a_rgb(mask, colores):
    h, w = mask.shape
    rgb = np.zeros((h, w, 3), dtype=np.uint8)
    for clase, color in colores.items():
        rgb[mask == clase] = color
    return rgb

def procesar_dataset(ruta_base):
    particiones = ['train', 'val', 'test']
    for particion in particiones:
        carpeta_masks = os.path.join(ruta_base, particion, 'masks')
        carpeta_salida = os.path.join(ruta_base, particion, 'RGB_masks')
        os.makedirs(carpeta_salida, exist_ok=True)

        for archivo in os.listdir(carpeta_masks):
            if archivo.endswith('.png') or archivo.endswith('.jpg'):
                ruta_mascara = os.path.join(carpeta_masks, archivo)
                mascara = np.array(Image.open(ruta_mascara).convert('L'))

                rgb = convertir_mascara_a_rgb(mascara, colores_clases)
                nombre_rgb = os.path.splitext(archivo)[0] + '_RGB.png'

                ruta_guardado = os.path.join(carpeta_salida, nombre_rgb)
                Image.fromarray(rgb).save(ruta_guardado)

# Directorios base
procesar_dataset('C:\\Users\\Gorge\\Desktop\\Dataset-of-weeds-in-potato-crops-in-the-province-of-Carchi-and-Imbabura-in-\\Balanced')
procesar_dataset('C:\\Users\\Gorge\\Desktop\\Dataset-of-weeds-in-potato-crops-in-the-province-of-Carchi-and-Imbabura-in-\\Unbalanced')

print("✅ Conversión completa.")
