import streamlit as st
st.set_page_config(
    page_icon= "🚎",
    page_title = "Bus Details",
    layout = 'wide',
)
from maindata import datta
from mapz import mapz
from custom_graph import gragh
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Swecha Organization", ['Data', 'Maps', 'Graphs'],
    icons = ['bi bi-table', 'bi bi-map', 'bi bi-bar-chart'], menu_icon = "cast", default_index = 1)
if selected == 'Data':
    datta()
elif selected == 'Maps':
    mapz()
elif selected == 'Graphs':
    gragh()