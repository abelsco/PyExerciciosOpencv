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
grafico.hist(img.ravel(), 256, [0, 256])
grafico.show()

cv.destroyAllWindows()
