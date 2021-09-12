import folium
import pandas
 
data = pandas.read_csv("volcano.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
 
def colour_purpose(elevation):
    if elevation < 1500:
        return "green"
    elif 1500<= elevation < 2500:
        return "red"
    else:
        return "purple"     

html = """<h4>Volcano information:</h4>
Height: %s m
"""
 
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius = 6, popup=folium.Popup(iframe),
    fill_color=colour_purpose(el), color=colour_purpose(el),fill_opacity=0.7))
 
 
map.add_child(fg)
map.save("Map_html_popup_simple.html")