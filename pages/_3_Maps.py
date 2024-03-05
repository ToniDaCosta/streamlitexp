import streamlit as st
from streamlit_folium import folium_static
import streamlit.components.v1 as components
import codecs
import folium
import requests

default_value = "Carrer de Pamplona 96 08018 Barcelona"
ad = st.text_input("Enter an address: ", default_value)

try:
    data = requests.get(f"https://geocode.xyz/{ad}?json=1").json()
    lat = data["latt"]
    lon = data["longt"]
    latlon = [lat, lon]
except:
    st.warning("Geocode doesn't want to work")
    latlon = [41.3977737, 2.1904561]

icon_ = folium.Icon(color = "blue",
                    prefix = "fa",
                    icon = "rocket",
                    icon_color = "black"
                    )

the_data = {"location": latlon, "tooltip": "Ironhack", "icon": icon_}
marker = folium.Marker(**the_data)

map_1 = folium.Map(location = latlon, zoom_start = 15)
marker.add_to(map_1)
folium_static(map_1)