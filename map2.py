#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu



import folium
import pandas as pd

m = folium.Map(location=(40.75, -74.125))
file = input("Enter CSV file name: ")
outputFile = input("Enter output file: ")
data = pd.read_csv(file)
data = data.fillna(0)
for i in range(len(data)):
    if not(data['LATITUDE'][i]== 0 and data['LONGITUDE'][i] == 0):
        folium.Marker(
            location = [data['LATITUDE'][i], data['LONGITUDE'][i]] 
        ).add_to(m)



m.save(outputFile)

