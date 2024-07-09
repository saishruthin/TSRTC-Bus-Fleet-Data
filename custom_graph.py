import streamlit as st
import pandas as pd
from final_data import dataset
import plotly.express as px
def graphing(df, x_axis, y_axis):
    fig = px.bar(df, x = x_axis, y = y_axis, title = f'{x_axis} vs {y_axis}')
    st.plotly_chart(fig, use_container_width=True)

def gragh():
    with open("title.css", 'r') as file:
        st.markdown(f"""<style>{file.read()}</style>""", unsafe_allow_html=True)
    st.markdown("""<div class = "custom-text-box">
    <div class = "text-content">Custom Graphs 📊</div>            
    </div>""", unsafe_allow_html=True)
    df = dataset()
    elementss = df.columns
    st1, st2 = st.columns(2)
    with st1:
        x_axis = st.selectbox("x axis?", elementss)
    with st2:
        y_axis = st.selectbox("y axis?", elementss)
    graphing(df, x_axis, y_axis)
    st.markdown("""
<div class = "caution-box">
<div class = "text">Please try to use Districts as x axis</div>                
</div>
""", unsafe_allow_html=True)