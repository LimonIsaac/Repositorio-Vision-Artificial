import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carga la imagen (ajusta el nombre del archivo si es necesario)
img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)

# Verifica si se cargó correctamente
if img is None:
    print("Error al cargar la imagen.")
    exit()

# Ecualización del histograma
img_eq = cv2.equalizeHist(img)

# Cálculo de histogramas
hist_orig = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_eq = cv2.calcHist([img_eq], [0], None, [256], [0, 256])

# Configuración de la figura
plt.figure(figsize=(10, 6))

# Imagen original
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')

# Histograma original
plt.subplot(2, 2, 2)
plt.plot(hist_orig, color='black')
plt.title('Histograma Original')
plt.xlim([0, 256])

# Imagen ecualizada
plt.subplot(2, 2, 3)
plt.imshow(img_eq, cmap='gray')
plt.title('Imagen Ecualizada')
plt.axis('off')

# Histograma ecualizado
plt.subplot(2, 2, 4)
plt.plot(hist_eq, color='black')
plt.title('Histograma Ecualizado')
plt.xlim([0, 256])

# Mostrar todo
plt.tight_layout()
plt.show()
