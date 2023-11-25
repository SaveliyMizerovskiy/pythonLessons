#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd

name = input("Give data name: ")
myVar = pd.read.csv(name)

myVar.plot(x="Year")
plt.show()