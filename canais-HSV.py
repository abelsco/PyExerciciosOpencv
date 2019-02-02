import cv2 as cv

img = cv.imread('1.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

matriz, saturacao, valor = cv.split(img)
cv.imshow('Original', img)
cv.imshow('Canal H', matriz)
cv.imshow('Canal S', saturacao)
cv.imshow('Canal V', valor)

img = cv.merge((matriz, saturacao, valor))
cv.imshow('Combinada', img)
img = cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.waitKey(0)
cv.destroyAllWindow()
