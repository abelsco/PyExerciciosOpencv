import cv2

img = cv2.imread('1.jpg')
azul, verde, vermelho = cv2.split(img)
cv2.imshow('Imagem', img)
cv2.imshow('Verde', verde)
cv2.imshow('Azul', azul)
cv2.imshow('Vermelho', vermelho)

cv2.imwrite('canal-azul.jpeg', azul)
cv2.imwrite('canal-verde.jpeg', verde)
cv2.imwrite('canal-vermelho.jpeg', vermelho)

cv2.waitKey(0)
cv2.destroyAllWindows()
