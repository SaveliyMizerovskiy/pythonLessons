#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu



import folium

m = folium.Map(location=(40.75, -74.125))

folium.Marker(
    location=[40.7678, -73.9645],
    popup="Hunter College",
).add_to(m)

m.save("nycMap.html")
