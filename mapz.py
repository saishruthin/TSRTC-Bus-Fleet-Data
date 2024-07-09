import folium
import streamlit as st
from streamlit_folium import st_folium
from final_data import final_data
def maps():
    df = final_data()
    telangana_coordinates = [18.1124, 79.0193]
    mappy = folium.Map(location = telangana_coordinates, zoom_start=7)
    for index,row in df.iterrows():
        folium.Marker(location = [row['latitude'], row['longitude']], popup = row['Districts'], icon = folium.Icon(color = 'red', icon = 'info-sign'), tooltip = row['Districts']).add_to(mappy)
    mapp = st_folium(mappy, width = 700, height = 600)
    
    if mapp['last_object_clicked'] is not None:
        clicked = mapp['last_object_clicked']
        lat, lng = clicked['lat'], clicked['lng']
        new_df = df[(df['latitude'] == lat) & (df['longitude'] == lng)]
        return new_df
    else:
        return None
def mapz():
    with open("title.css", 'r') as file:
        st.markdown(f"""<style>{file.read()}</style>""", unsafe_allow_html=True)
    st.markdown("""
<div class = "custom-text-box">
<div class = "text-content">Map Filter 📍</div>                
</div>
""", unsafe_allow_html=True)
    st.markdown("""
<div class = "custom-subheader">Please select the location:</div>
""", unsafe_allow_html=True)
    s1, s2 = st.columns([2,1])
    with s1:
        kpis = maps()
    with s2:
        if kpis is None:
            st.markdown("""<div class = "caution-box">⚠️ You haven't selected location. Please select</div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class = 'custom-subheader'>{kpis['Districts'].values[0]} 📍</div>""", unsafe_allow_html=True)
            st.markdown(f"""
<div class = "kpi-container">
<div>
<div class = "kpi-label">Daily Operated length</div>
<div class = "kpi-value">{kpis['Daily Operated Length (Kms.)'].values[0]} kms</div>
</div>
</div>
""", unsafe_allow_html=True)
            st.markdown(f"""
<div class = "kpi-container">
<div>
<div class = "kpi-label">Bus Fleet details</div>
<div class = "kpi-value">{kpis['RTC Fleet of Buses'].values[0]}</div>
</div>
</div>
""", unsafe_allow_html=True)
            st.markdown(f"""
<div class = "kpi-container">
<div>
<div class = "kpi-label">Bus depots</div>
<div class = "kpi-value">{kpis['RTC Bus Depots'].values[0]}</div>
</div>                        
</div>
""", unsafe_allow_html=True)

    
        
mapz()
         