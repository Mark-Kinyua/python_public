import folium
import pandas

volcano = pandas.read_csv("Volcanoes.txt")
world = open('world.json', 'r', encoding='utf-8-sig').read()
lat = list(volcano["LAT"])
lon = list(volcano["LON"])
elev = list(volcano["ELEV"])


def color_produce(elevation):
    if elevation < 1000:
        return "green"
    elif elevation < 2000:
        return "blue"
    elif elevation < 3000:
        return "orange"
    else:
        return "red"


mp = folium.Map(location=[48.776798, -121.810997], zoom_start=4)

fgv = folium.FeatureGroup(name="Volcano")
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el) + " m",
                                      fill_color=color_produce(el), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(
    folium.GeoJson(world, style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
    else 'red'}))

mp.add_child(fgv)
mp.add_child(fgp)
mp.add_child(folium.LayerControl())

mp.save("Map1.html")
