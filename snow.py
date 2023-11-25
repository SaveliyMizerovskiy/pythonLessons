#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu

import matplotlib.pyplot as plt
import numpy as np

name = input("Name of file: ")
ca = plt.imread(name)   
countSnow = 0            
t = 0.75                 

for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
               countSnow = countSnow + 1

print("Snow count is", countSnow)