import cv2
import numpy as np

# === OBJETIVO 1: Encontrar similitudes entre imágenes con rotación ===
# Cargar imagen base y la imagen donde se buscarán similitudes
img1 = cv2.imread('opencv-feature-matching-template.jpg', 0)  # imagen a buscar (template)
img2 = cv2.imread('opencv-feature-matching-image.jpg', 0)    # imagen donde se buscará (escena)

# Inicializar detector ORB
orb = cv2.ORB_create()

# Detectar keypoints y descriptores
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Comparar los descriptores con BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

# Dibujar los mejores 20 matches
img_match = cv2.drawMatches(img1, kp1, img2, kp2, matches[:20], None, flags=2)

cv2.imshow('Similitudes por ORB', img_match)

# === OBJETIVO 2: Extracción de fondo por movimiento en video ===
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    fgmask = fgbg.apply(frame)  # máscara del fondo

    # Mostrar resultados
    cv2.imshow('Video Original', frame)
    cv2.imshow('Fondo extraído por movimiento', fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
