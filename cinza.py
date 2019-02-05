import cv2 as cv
'''
Exibe a Imagem en tons de Cinza
'''
img = cv.imread('1.jpg')
cv.imshow('Original', img)

# cvtColor -> converte a imagem para um espaço de cores especifico
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Imagem', img)

cv.waitKey(0)
cv.destroyAllWindows()
