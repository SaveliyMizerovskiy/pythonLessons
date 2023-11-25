#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu

import matplotlib.pyplot as plt
import numpy as np

size = int(input("Size: "))
img2Name = input("PNG Name: ")

img = np.ones((size,size,3))

img[:,:,0:1]=1
img[:,:,2]=0
img[::2,:,0]=1
img[::2,:,1]=0
img[::2,:,2]=1



plt.imsave(img2Name,img)