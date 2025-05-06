import cv2

# Cargar imagen
img = cv2.imread('watch.jpg')  # Usa tu imagen

# Dibujar un rectángulo (x1,y1) a (x2,y2)
cv2.rectangle(img, (100, 50), (300, 200), (0, 255, 0), 2)

# Dibujar un círculo
cv2.circle(img, (200, 125), 40, (255, 0, 0), 2)

# Dibujar una línea
cv2.line(img, (100, 50), (300, 200), (0, 0, 255), 2)

# Escribir texto
cv2.putText(img, 'Reloj', (100, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

# Seleccionar ROI (porciones de la imagen)
roi = img[50:200, 100:300]  # misma región que el rectángulo

# Mostrar imagen original con dibujo
cv2.imshow('Imagen con dibujos', img)

# Mostrar ROI
cv2.imshow('Region de Interes (ROI)', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
