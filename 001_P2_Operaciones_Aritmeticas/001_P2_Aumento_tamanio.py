import cv2

img = cv2.imread('watch.jpg')  
bigger_img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)  # Doble de tamaño

cv2.imshow('Imagen aumentada', bigger_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
