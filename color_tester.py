import cv2 as cv
import numpy as np

# Inicializar ventana de ajustes
cv.namedWindow("Ajustes LAB")
cv.resizeWindow("Ajustes LAB", 600, 300)

# Valores iniciales para el azul (en formato LAB para OpenCV)
azulBajo = np.array([54, 122, 25], dtype=np.uint8)
azulAlto = np.array([148, 164, 121], dtype=np.uint8)

# Crear trackbars para los rangos LAB
cv.createTrackbar("L_min", "Ajustes LAB", azulBajo[0], 255, lambda x: None)
cv.createTrackbar("a_min", "Ajustes LAB", azulBajo[1], 255, lambda x: None)
cv.createTrackbar("b_min", "Ajustes LAB", azulBajo[2], 255, lambda x: None)
cv.createTrackbar("L_max", "Ajustes LAB", azulAlto[0], 255, lambda x: None)
cv.createTrackbar("a_max", "Ajustes LAB", azulAlto[1], 255, lambda x: None)
cv.createTrackbar("b_max", "Ajustes LAB", azulAlto[2], 255, lambda x: None)

# Trackbars para operaciones morfológicas
cv.createTrackbar("Kernel", "Ajustes LAB", 5, 20, lambda x: None)
cv.createTrackbar("Erosiones", "Ajustes LAB", 1, 5, lambda x: None)
cv.createTrackbar("Dilataciones", "Ajustes LAB", 1, 5, lambda x: None)

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Obtener valores actuales de los trackbars
    L_min = cv.getTrackbarPos("L_min", "Ajustes LAB")
    a_min = cv.getTrackbarPos("a_min", "Ajustes LAB")
    b_min = cv.getTrackbarPos("b_min", "Ajustes LAB")
    L_max = cv.getTrackbarPos("L_max", "Ajustes LAB")
    a_max = cv.getTrackbarPos("a_max", "Ajustes LAB")
    b_max = cv.getTrackbarPos("b_max", "Ajustes LAB")

    # Actualizar rangos LAB
    azulBajo = np.array([L_min, a_min, b_min], dtype=np.uint8)
    azulAlto = np.array([L_max, a_max, b_max], dtype=np.uint8)

    # Convertir a LAB y crear máscara
    lab = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
    mask = cv.inRange(lab, azulBajo, azulAlto)

    # Operaciones morfológicas (kernel dinámico)
    kernel_size = cv.getTrackbarPos("Kernel", "Ajustes LAB")
    erosiones = cv.getTrackbarPos("Erosiones", "Ajustes LAB")
    dilataciones = cv.getTrackbarPos("Dilataciones", "Ajustes LAB")

    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    eroded_mask = cv.erode(mask, kernel, iterations=erosiones)
    dilated_mask = cv.dilate(eroded_mask, kernel, iterations=dilataciones)
    mask = dilated_mask

    # Mostrar resultados
    cv.imshow("Frame Original", frame)
    cv.imshow("Máscara LAB", mask)
    cv.imshow("Azul Detectado", cv.bitwise_and(frame, frame, mask=mask))

    # Salir con 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
