import cv2

img = cv2.imread('watch.jpg')  
negative_img = 255 - img  # Inversión de colores

cv2.imshow('Imagen negativa', negative_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
