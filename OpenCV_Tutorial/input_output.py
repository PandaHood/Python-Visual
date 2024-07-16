import os
import cv2
# read image 
image_path = "OpenCV_Tutorial\\bird_in.jpg"

img = cv2.imread(image_path)

#write image
cv2.imwrite("OpenCV_Tutorial\\bird_out.jpg",img)

# visualize image
cv2.imshow('image', img)
cv2.waitKey(0)