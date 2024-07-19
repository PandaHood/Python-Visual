import os
import cv2
# read image 
image_path = "OpenCV_Tutorial\\bird_in.jpg"

img = cv2.imread(image_path)

print(img.shape)

img = cv2.resize(img,(1920,1080))

print(img.shape)

img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)


# visualize image
cv2.imshow('image', img)
cv2.waitKey(0)

img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# visualize image
cv2.imshow('image', img)
cv2.waitKey(0)

print(img.shape)

#write image
cv2.imwrite("OpenCV_Tutorial\\bird_out.jpg",img)