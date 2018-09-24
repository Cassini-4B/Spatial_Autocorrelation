import folium
from folium import plugins
from folium.plugins import HeatMap


def create_map(data):
    m = folium.Map(location=[39.986052, -91.194961], tiles='Cartodb Positron', zoom_start=7)

    HeatMap(data, radius=25, gradient={.4: 'teal', .65: 'red', 1: 'yellow'}).add_to(m)
    
    html_string = m.get_root().render()
    return html_string