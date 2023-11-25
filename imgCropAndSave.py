#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu

import matplotlib.pyplot as plt
import numpy as np

name = input("Enter file name: ")
img = plt.imread(name)

outputName = input("Enter file name: ")
height = img.shape[0]
width = img.shape[1]

cropped = img[height//2:, :width//2, :]

#plt.imshow(cropped)
#plt.show()

plt.imsave(outputName, cropped)