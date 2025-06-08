import cv2
import numpy as np

# Cargar imagen
img = cv2.imread('opencv-python-foreground-extraction-tutorial.jpg')
clone = img.copy()

# Seleccionar ROI manualmente (se abre una ventana para elegirlo)
x, y, w, h = cv2.selectROI('Selecciona ROI', img, False, False)
cv2.destroyWindow('Selecciona ROI')

# Extraer ROI (Región de Interés)
roi = clone[y:y+h, x:x+w]

# Crear una máscara del mismo tamaño que la imagen, con todo negro
mask = np.zeros_like(img)

# Rellenar la zona del ROI con blanco en la máscara
mask[y:y+h, x:x+w] = 255

# Aplicar la máscara para extraer solo el ROI (fondo en negro)
solo_roi = cv2.bitwise_and(clone, mask)

# Convertir el ROI a escala de grises para encontrar esquinas
roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
roi_gray = np.float32(roi_gray)

# Encontrar esquinas con Harris
corners = cv2.cornerHarris(roi_gray, 2, 3, 0.04)
roi_with_corners = roi.copy()
roi_with_corners[corners > 0.01 * corners.max()] = [0, 0, 255]

# Mostrar resultados
cv2.imshow('ROI extraído', roi)
cv2.imshow('Fondo eliminado', solo_roi)
cv2.imshow('Esquinas detectadas', roi_with_corners)

cv2.waitKey(0)
cv2.destroyAllWindows()
