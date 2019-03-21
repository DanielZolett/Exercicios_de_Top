import numpy as np
import cv2 as cv
import os

elemt_estru = np.array([[255,255,255],
                       [255,255,255],
                       [255,255,255]])
img = cv.imread ('borbo.png',0)

# retirando elementos indesejados
for i in range (0,290,1):
    for j in range(500,800,1):
        img[i][j] = 0

for i in range (550,600,1):
    for j in range(0,100,1):
        img[i][j] = 0

#criando buracos

for i in range (500,525,1):
    for j in range(325,400,1):
        img[i][j] = 0

alt,lar = img.shape
x = np.zeros((alt,lar)) # criando matriz x

print (img.shape)

img_comp = np.copy(img)

for i in range (600):
    for j in range(800):
        img_comp[i][j] = ~img[i][j]


x [500][325] = 255

for i in range (500,550,1):
    for j in range(325,410,1):
        if elemt_estru[1][1] == 255 and x[i][j] == 255:
            for a in range(2):
                for b in range(2):
                    x[i+a][j+b] = elemt_estru[a][b]
                    x[i+a][j+b] = img_comp[i+a][j+b] and x[i+a][j+b]


corrigido = np.copy(img)

for i in range (500,550,1):
    for j in range(325,410,1):
        corrigido[i][j] = img[i][j] + x[i][j]

cv.imshow('imagem sem alteracao',img)
cv.imshow('imagem alterada',img_comp)
cv.imshow('imagem sem burracos',corrigido)

cv.waitKey(0)
cv.destroyAllWindows()