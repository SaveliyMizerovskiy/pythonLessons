#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
pop.plot(x="Year")
#plt.show()
bor = input("Enter borough: ")
avgP = pop[bor].mean()
maxP = pop[bor].max()
print("Average population: " + str(avgP))
print("Max Population:" + str(maxP))
