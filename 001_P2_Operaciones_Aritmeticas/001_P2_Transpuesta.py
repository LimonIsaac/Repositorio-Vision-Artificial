import cv2

img = cv2.imread('watch.jpg')  
transposed_img = cv2.transpose(img)  # Aplicar transposición

cv2.imshow('Imagen transpuesta', transposed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
