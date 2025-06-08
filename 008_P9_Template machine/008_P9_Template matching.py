import cv2
import numpy as np

# Cargar la imagen principal (donde se buscará el patrón)
img = cv2.imread('opencv-template-matching-python-tutorial.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Cargar la imagen del template (patrón a buscar)
template = cv2.imread('opencv-template-for-matching.jpg', 0)
h, w = template.shape

# Aplicar template matching
res = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)

# Umbral de coincidencia
threshold = 0.85
loc = np.where(res >= threshold)

# Dibujar rectángulos para cada coincidencia encontrada
for pt in zip(*loc[::-1]):  # Cambia x e y
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

# Mostrar resultados
cv2.imshow('Detección por Template Matching', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
