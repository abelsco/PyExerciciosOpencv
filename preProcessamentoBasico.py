import cv2 as cv
'''
Pre Processamento
Processo que busca realçar objetos/características de interesse em imagens
é feito para facilitar o processo de segmentação da Imagem

---------------------------------------------------------------
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
print('{} pixels'.format(int(img.size/img.shape[2])))

'''
Operações aritiméticas
Permite adcionar conteúdo e/ou mesclar imagens (mesma dimensão e tipo)
**Possibilidade de overflow (operação gerar um numero fora da faixa de
representação da imagem)
Ex.: 8 bits -> 256 possibilidades
[0, 14] = 255
[0, 14] += 15
[0, 14] = 270 -> ERRO

Adição
imgRes = cv2.add(imgA, imgB)
imgRes = cv2.add(img, 40) # mais claro
imgRes = cv2.add(img, -40)

Subtração
imgRes = cv2.subtract(imgA, imgB)
imgRes = cv2.subtract(img, 40) # mais escuro
imgRes = cv2.subtract(img, -40)
== Mesma ideia para as outras Operações

Mistura
Funciona como a soma, porem com pesos diferentes para as imagens(transparência)
quanto menor o peso mais tranparente a imagem fica.
addWeighted(src1, alpha, src2, beta, gamma)
==>srcx -> Matrizes referentes as imagens
==>alpha/beta -> Intensidade das imagens (peso)
==>gamma -> Escalar
'''
