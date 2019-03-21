import numpy as np
import cv2 as cv

elemt_estru = np.ones((10,10),np.uint8)
img = cv.imread ('borbo.png',0)

for i in range (0,300,1):
    for j in range(500,800,1):
        img[i][j] = 1

for i in range (550,600,1):
    for j in range(0,100,1):
        img[i][j] = 1

#img_cinza = cv.cvtColor(img,cv.IMREAD_COLOR)

print (img.shape)
img_comp = np.copy(img)
borda = np.copy(img)

img_comp = cv.erode(img_comp,elemt_estru,iterations=1)


borda = img-img_comp

cv.imshow('imagem sem alteracao',img)
cv.imshow('imagem alterada',img_comp)
cv.imshow('imagem borda',borda)

cv.waitKey(0)
cv.destroyAllWindows()
