import cv2
import numpy as np

img = cv2.imread('watch.jpg')  
darker_img = cv2.subtract(img, np.array([50.0]))  # Reducir brillo en 50 niveles

cv2.imshow('Imagen con menor brillo', darker_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
