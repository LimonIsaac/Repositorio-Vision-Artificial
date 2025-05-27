import cv2
import numpy as np

# Iniciar captura de video desde webcam
cap = cv2.VideoCapture(0)

# Crear kernel para operaciones morfológicas
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (100, 100))

# Variable para guardar el frame anterior (para flancos)
prev_frame = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Filtro gaussiano (lineal)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)

    # TopHat (resalta detalles claros)
    tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)

    # BlackHat (resalta detalles oscuros)
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

    # Flanco positivo y negativo
    if prev_frame is not None:
        diff = cv2.absdiff(gray, prev_frame)
        flanco_positivo = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
        flanco_negativo = cv2.threshold(cv2.subtract(prev_frame, gray), 25, 255, cv2.THRESH_BINARY)[1]

        cv2.imshow('Flanco Positivo', flanco_positivo)
        cv2.imshow('Flanco Negativo', flanco_negativo)

    prev_frame = gray.copy()

    # Mostrar resultados
    cv2.imshow('Webcam - Original', frame)
    cv2.imshow('Filtro Gaussiano', blur)
    cv2.imshow('TopHat', tophat)
    cv2.imshow('BlackHat', blackhat)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
