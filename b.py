import cv2
import time
# Initialize the webcam
cam = cv2.VideoCapture(0)
cv2.namedWindow("Press SPACE to capture")

img_counter = 0
time.sleep(1)
ret, frame = cam.read()

img_name = f"opencv_frame_{img_counter}.png"
cv2.imwrite(img_name, frame)


cam.release()
cv2.destroyAllWindows()
