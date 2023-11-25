#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu

import pandas as pd

file = input("File name: ")
data = pd.read_csv(file)
print(data["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])