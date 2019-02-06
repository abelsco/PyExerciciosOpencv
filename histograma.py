import cv2 as cv
import numpy as np
from matplotlib import pyplot as grafico

'''
Histograma é a distribuição de frequência dos niveis de cinza em relação ao
numero de amostras
Aborda:
-> Intensidade luminosa
-> Contraste
'''
img = cv.imread('3.bmp')
cv.imshow('Cinza', cv.cvtColor(img, cv.COLOR_RGB2GRAY))

# imread('', 0) -> abre a imagem em tons de cinza
img = cv.imread('3.bmp', 0)

totalPixelsPreto = totalPixelsBranco = 0
# forma não usual/ pouco utilizada
for x in range(0, img.shape[0]):
    for y in range(0, img.shape[1]):
        if img[x, y] == 255:
            totalPixelsPreto += 1
        else:
            totalPixelsBranco += 1
print('Pixels Bracos({}) Pretos({})'.format(totalPixelsBranco, totalPixelsPreto))
# Fim

# hist -> função que realiza o histograma, pertence ao matplotlib
# ravel() -> transforma a imagem em um vetor contendo os pixels
grafico.hist(img.ravel(), 256, [0, 256])
grafico.show()

cv.destroyAllWindows()

# Histograma imagem colorida
img = cv.imread('3.bmp')

azul, verde, vermelho = cv.split(img)

grafico.hist(azul.ravel(), 256, [0, 256])
grafico.figure()
grafico.hist(verde.ravel(), 256, [0, 256])
grafico.figure()
grafico.hist(vermelho.ravel(), 256, [0, 256])
grafico.show()

'''
*Equalização Histograma (equalizeHist())

=Exposição a Luz=
Superexpostas - Envolvem mais elementos a direita, quanto mais prox de 256 mais
claro a imagem é.
Subexpostas - O contrario de superexposta, possuí valores proximos do 0.

=Contraste=
Alto contraste - Histograma com uma distribuição de valores elevada,
consequêntemente, envolve histogramas mais largos.
Baixo contraste - Histograma com valores concentrados em uma faixa pequena.

'''
# Equalização imagem cinza
img = cv.imread('4.jpg', 0)
imgEq = cv.equalizeHist(img)

cv.imshow('Orig', img)
cv.imshow('Eq', imgEq)

grafico.hist(img.ravel(), 256, [0, 256])
grafico.figure()
grafico.hist(imgEq.ravel(), 256, [0, 256])
grafico.show()

cv.waitKey(0)
cv.destroyAllWindows()
# Equalização imagem colorida
img = cv.imread('5.jpg')
img = cv.cvtColor(img, cv.COLOR_RGB2HSV)
matriz, saturacao, valor = cv.split(img)

valorEq = cv.equalizeHist(valor)
imgEq = cv.merge((matriz, saturacao, valorEq))
img = cv.cvtColor(img, cv.COLOR_HSV2RGB)
imgEq = cv.cvtColor(imgEq, cv.COLOR_HSV2RGB)
cv.imshow('Orig', img)
cv.imshow('Eq', imgEq)

grafico.hist(valor.ravel(), 256, [0, 256])
grafico.figure()
grafico.hist(valorEq.ravel(), 256, [0, 256])
grafico.show()

cv.waitKey(0)
cv.destroyAllWindow()
