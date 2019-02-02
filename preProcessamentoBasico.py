import cv2 as cv
'''
Valor numérico do pixel na posição 150, 150 da matriz de pixels
que representa a imagem

acaso necessária a alteração do valor é feita de forma matricial
imagem[150, 150] = [0, 0, 0]
'''


def printValor(img, tag):
    valorPixel = img[150, 150]
    print('[{}] {}'.format(tag, valorPixel))


# RGB
img = cv.imread('2.jpg')
printValor(img, 'RGB')

# GRAY
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
printValor(img, 'GRAY')

# HSV
img = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
img = cv.cvtColor(img, cv.COLOR_RGB2HSV)
printValor(img, 'HSV')

# Imprimindo numero de linhas, colunas, e canais da Imagem
print('[{i}] Linhas:{i[0]} Colunas:{i[1]} Canais:{i[2]}'.format(i=img.shape))

# Tamanho da imagem (Linhas x Colunas)/Canais
print('{} pixels'.format(int(img.size/3)))
