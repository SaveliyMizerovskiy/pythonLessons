#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd


fileName = input("Enter file name:")
homeless = pd.read_csv(fileName)
homeless['Fraction Children'] = homeless['Total Children in Shelter'] / homeless['Total Individuals in Shelter']
homeless.plot(x = "Date of Census", y = "Fraction Children")


outputName = input("Enter output file name:")
plt.savefig(outputName)
#plt.show()