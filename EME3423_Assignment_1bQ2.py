
import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Keep same size for stacking
    frame = cv2.resize(frame, (640, 480))

    # --- Original (color) -> TOP RIGHT ---
    original = frame.copy()

    # Prepare grayscale once (for Canny + Gaussian Blur)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # --- Canny edges (B/W) -> TOP LEFT ---
    edges = cv2.Canny(gray, 50, 150)
    edges_3c = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # --- HSV (color) -> BOTTOM LEFT ---
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # --- Gaussian Blur (B/W grayscale) -> BOTTOM RIGHT ---
    blur_bw = cv2.GaussianBlur(gray, (11, 11), 0)
    blur_3c = cv2.cvtColor(blur_bw, cv2.COLOR_GRAY2BGR)

    # Build 2×2 grid:
    # [Canny   | Original]
    # [HSV     | Gaussian Blur (B/W)]
    top = np.hstack((edges_3c, original))
    bottom = np.hstack((hsv, blur_3c))
    grid = np.vstack((top, bottom))

    cv2.imshow("Q2 - 2x2 Grid", grid)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
