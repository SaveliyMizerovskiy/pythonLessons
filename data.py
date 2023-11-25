#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu


import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
pop.plot(x="Year")

bor = input("Enter borough: ")
name = input("File Name: ")

pop['Fraction'] = pop[bor]/pop['Total']
pop.plot(x = 'Year', y = 'Fraction')

fig = plt.gcf()
fig.savefig(name)