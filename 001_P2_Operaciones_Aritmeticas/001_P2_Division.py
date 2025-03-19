import cv2
import numpy as np

img = cv2.imread('watch.jpg')  
low_intensity = cv2.divide(img, np.array([2.0]))  # Reducir la intensidad a la mitad

cv2.imshow('Imagen con menor intensidad', low_intensity)
cv2.waitKey(0)
cv2.destroyAllWindows()
