import cv2

img = cv2.imread("panda.jpg")

grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresholdimg = cv2.threshold(grayimg, 180,255, cv2.THRESH_BINARY)[1]

cv2.imshow('original',img)

cv2.imshow('threshold.jpg',thresholdimg )

