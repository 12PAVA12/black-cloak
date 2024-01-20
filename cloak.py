import cv2
import numpy as np

# Start video capture
cap = cv2.VideoCapture(0)  # Use 0 for the default camera, or provide the path to a video file

# Read the image to be shown when the black object is masked
image = cv2.imread('path/to/your/image.jpg')  # Replace with the actual path to your image

while True:
    # Read frames from the video
    ret, frame = cap.read()

    # Resize the image and the video to 640x480
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    # Create an array of RGB for faint black color shade and dark shade of black
    l_black = np.array([0, 0, 0], dtype=np.uint8)
    u_black = np.array([50, 50, 50], dtype=np.uint8)

    # Create a mask using cv's inRange() function
    mask = cv2.inRange(frame, l_black, u_black)

    # Use np.where() to return frame if the value of the mask is 0, otherwise use the image
    result = np.where(mask[:, :, None].astype(bool), image, frame)

    # Show the real video and masked video
    cv2.imshow('Real Video', frame)
    cv2.imshow('Masked Video', result)

    # Break the loop if the user presses "Esc" or "Q"
    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'):
        break

# Release the video capture object and close the windows
cap.release()
cv2.destroyAllWindows()
