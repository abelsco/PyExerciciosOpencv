import cv2 as cv

'''
*Ruídos
Variações aleatória sofridas pelo sinal.

=>Captura:
Provocado pelo ambiente ou vibrações e/ou imperfeições da câmera, ou ainda por
ruido elétrico.
=>Amostragem:
Sinal digital não representa a imagem verdadeira.
=>Processamento:
Gerado por conta de overflow no calculo com números inteiros/ponto flutuante.
Geralmente no contorno dos objetos.
=>Codificação:
Gerado pela compressão de imagens.
=>Oclusão:
Informação desejada da imagem está parcialmente ou totamente obstruida.
Algumas vezes é possível reconhecer a imagem.
=>Sal e pimenta:
Pixels aleatorios con intensidades aleatórias dispostos de maneira aleatória
na imagem.(Não é comum para sensores modernos).
=>Gaussiano:
Variação aleatoria do sinal seguindo a distribuição de Gauss.
Geralmente é provocado por problemas de iluminação e/ou alta temperatura.
=>Ruído Binário:
Gerado durante o processo de binarização.
'''
