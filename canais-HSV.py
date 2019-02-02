import cv2 as cv

img = cv.imread('1.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

matriz, saturacao, valor = cv.split(img)
cv.imshow('Original', img)
cv.imshow('Canal H', matriz)
cv.imshow('Canal S', saturacao)
cv.imshow('Canal V', valor)

cv.waitKey(0)
cv.destroyAllWindow()
