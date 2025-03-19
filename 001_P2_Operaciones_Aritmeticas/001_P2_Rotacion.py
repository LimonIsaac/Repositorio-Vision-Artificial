import cv2
import numpy as np

img = cv2.imread('watch.jpg')  
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)  # Rotación de 45 grados
rotated_img = cv2.warpAffine(img, matrix, (w, h))

cv2.imshow('Imagen rotada', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
