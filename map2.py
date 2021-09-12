                                #VOLCANO LOCATION MARKERS#
import pandas
import folium
data = pandas.read_csv("volcano.txt")
    
map = folium.Map(location=[38.883333,-77.016667],zoom_start=6, tiles = "Stamen Terrain")
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

fgv = folium.FeatureGroup(name="Volcanoes")

for lt , ln ,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius = 6, popup=str(el) + 'm', 
    fill_color=colour_purpose(el), color=colour_purpose(el),fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json' , 'r' , encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})) 

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map_layercontrol.html")