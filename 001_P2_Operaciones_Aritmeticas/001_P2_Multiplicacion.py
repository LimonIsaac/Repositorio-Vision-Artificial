import cv2
import numpy as np

img = cv2.imread('watch.jpg')  
higher_contrast = cv2.multiply(img, np.array([1.5]))  # Aumentar contraste 1.5x

cv2.imshow('Imagen con mayor contraste', higher_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()
