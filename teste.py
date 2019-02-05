import cv2
'''
Apenas para teste da biblioteca
possui comandos básicos
'''
# imread('') -> Le a imagem e armazena em uma matriz de pixels
img = cv2.imread('1.jpg')

# split() -> Separa os canais das imagem em matrizes diferentes
# Importante lembrar que o OpenCV organiza BGR e não RGB
azul, verde, vermelho = cv2.split(img)

# imshow('', ) -> Exibe a Imagem
cv2.imshow('Imagem', img)
cv2.imshow('Verde', verde)
cv2.imshow('Azul', azul)
cv2.imshow('Vermelho', vermelho)

# imwrite('', ) -> Salva a imagem
cv2.imwrite('canal-azul.jpeg', azul)
cv2.imwrite('canal-verde.jpeg', verde)
cv2.imwrite('canal-vermelho.jpeg', vermelho)

# waitKey(delay) -> Espera o evento de uma tecla, se ocorre executa com o delay
cv2.waitKey(0)
# destroyAllWindows() -> Fecha as janelas que o imshow('', ) abriu
cv2.destroyAllWindows()
