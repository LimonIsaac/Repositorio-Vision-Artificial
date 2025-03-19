import cv2
import numpy as np

img = cv2.imread('watch.jpg')  
(h, w) = img.shape[:2]
matrix = np.float32([[1, 0, 50], [0, 1, 100]])  # Mover 50px en X, 100px en Y
translated_img = cv2.warpAffine(img, matrix, (w, h))

cv2.imshow('Imagen trasladada', translated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
