import cv2
import numpy as np

img = cv2.imread('watch.jpg')  # Cargar imagen a color
brighter_img = cv2.add(img, np.array([50.0]))  # Aumentar brillo en 50 niveles

cv2.imshow('Imagen con mayor brillo', brighter_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
