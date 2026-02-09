
import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Resize for uniform layout
        frame_resized = cv2.resize(frame, (320, 240))

        # Create flipped versions
        flip_h = cv2.flip(frame_resized, 1)   # Horizontal flip
        flip_v = cv2.flip(frame_resized, 0)   # Vertical flip
        flip_hv = cv2.flip(frame_resized, -1) # Horizontal + Vertical

        # Arrange into a 2×2 grid
        top_row = np.hstack((frame_resized, flip_h))
        bottom_row = np.hstack((flip_v, flip_hv))
        combined = np.vstack((top_row, bottom_row))

        # Show in one window
        cv2.imshow("Four Webcam Outputs", combined)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
