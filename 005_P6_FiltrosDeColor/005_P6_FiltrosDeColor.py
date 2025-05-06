import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cargar imagen
img = cv2.imread('Flor.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Rangos HSV para rojo (considera que está dividido en dos partes)
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)

lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])
mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)

mask_red = cv2.bitwise_or(mask_red1, mask_red2)
res_red = cv2.bitwise_and(img, img, mask=mask_red)

# Rango HSV para verde
lower_green = np.array([36, 50, 70])
upper_green = np.array([89, 255, 255])
mask_green = cv2.inRange(hsv, lower_green, upper_green)
res_green = cv2.bitwise_and(img, img, mask=mask_green)

# Rango HSV para azul
lower_blue = np.array([90, 60, 70])
upper_blue = np.array([128, 255, 255])
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
res_blue = cv2.bitwise_and(img, img, mask=mask_blue)

# Mostrar resultados
titles = ['Original', 'Rojo', 'Verde', 'Azul']
images = [img, res_red, res_green, res_blue]

plt.figure(figsize=(12, 6))
for i in range(4):
    plt.subplot(1, 4, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
