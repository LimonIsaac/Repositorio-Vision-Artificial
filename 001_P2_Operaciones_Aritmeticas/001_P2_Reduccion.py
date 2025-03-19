import cv2

img = cv2.imread('watch.jpg')  
smaller_img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)  # Mitad de tamaño

cv2.imshow('Imagen reducida', smaller_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
