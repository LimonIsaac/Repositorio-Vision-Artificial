import cv2
import numpy as np

# Iniciar la captura de video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Laplaciano
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))

    # Sobel X
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    sobelx = np.uint8(np.absolute(sobelx))

    # Sobel Y
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    sobely = np.uint8(np.absolute(sobely))

    # Canny
    canny = cv2.Canny(gray, 100, 200)

    # Mostrar imágenes
    cv2.imshow('Webcam - Original', frame)
    cv2.imshow('Laplaciano', laplacian)
    cv2.imshow('Sobel X', sobelx)
    cv2.imshow('Sobel Y', sobely)
    cv2.imshow('Canny', canny)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
