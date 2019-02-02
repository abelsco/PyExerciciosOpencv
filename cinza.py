import cv2 as cv

img = cv.imread('1.jpg')
cv.imshow('Original', img)
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Imagem', img)

cv.waitKey(0)
cv.destroyAllWindows()
