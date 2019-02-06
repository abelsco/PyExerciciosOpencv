import cv2 as cv
import numpy as np

'''
Tranformação geometrica:
Rotação:
>getRotationMatrix2D(center, angle, scale) -> Obtem uma matriz de rotação.
==>center -> Indica o centro da imagem (X, Y)
==>angle -> Define o ângulo desejado para rotacionar [0, 360]
==>scale -> Escala para imagem
>warpAffine(src, matriz, dsize) -> Gera a imagem rotacionada.
==>src -> Mesma coisa que o .this
==>matriz -> matriz de rotação.
==>dsize -> Tamanho da imagem rotacionada.
'''

img = cv.imread('1.jpg')
linhas, colunas = img.shape[:2]

matriz = cv.getRotationMatrix2D((colunas / 2, linhas / 2), 90, 1)
imgRot = cv.warpAffine(img, matriz, (colunas, linhas))
print(img.shape)

cv.imshow('Rot', imgRot)
cv.waitKey(0)
cv.destroyAllWindows()

matriz = np.float32([[1, 0, 32], [0, 1, 30]])
imgDesloc = cv.warpAffine(img, matriz, (colunas, linhas))

cv.imshow('Desloc', imgDesloc)
cv.waitKey(0)
cv.destroyAllWindows()

'''
*Ajuste Escala
resize(src, dst, fx, fy, interpolation)
'''

# img = cv.imread('5.jpg')
img = cv.resize(cv.imread('5.jpg'), None, None, .5, .5, cv.INTER_NEAREST)

cv.imshow('Resultado', img)
cv.waitKey(0)
cv.destroyAllWindows()

'''

'''
