import streamlit as st
from donut import donut
import ssl
import pandas as pd
import plotly.express as px
from final_data import dataset
def datta():
    with open("title.css", 'r') as file:
        st.markdown(f"""<style>{file.read()}</style>""", unsafe_allow_html=True)
    with open('style.css', 'r') as style:
        st.markdown(f"""<style>{style.read()}</style>""", unsafe_allow_html=True)
    with open('script.js', 'r') as script:
        st.markdown(f"""<script>{script.read()}</script>""", unsafe_allow_html=True)
    st.markdown("""<div class = "custom-text-box">
    <div class = "text-content">Bus Details 🚎</div>
    </div>""", unsafe_allow_html=True)
    df = dataset()
    filter = st.selectbox("What district do you want to select", pd.unique(df['Districts']))
    new_df = df[df['Districts'] == filter]
    s1, s2, s3 = st.columns(3, gap = 'medium')
    with s1:
        st.markdown(f"""
<div class = 'kpi-container'>
<div class = 'kpi-label'>Length from {filter} is</div>
<div class = 'kpi-value'>{round(int(new_df['Daily Operated Length (Kms.)'].iloc[0]))} km</div>
</div>
""", unsafe_allow_html=True)
    with s2:
        st.markdown(f"""
<div class = 'kpi-container'>
<div class = 'kpi-label'>Bus Depots from {filter}</div>
<div class = 'kpi-value'>{round(int(new_df['RTC Bus Depots'].iloc[0]))}</div>                        
</div>
""", unsafe_allow_html=True)
    with s3:
        st.markdown(f"""
<div class = 'kpi-container'>
<div class = 'kpi-label'>Bus Fleets from {filter}</div>
<div class = 'kpi-value'>{round(int(new_df['RTC Fleet of Buses'].iloc[0]))}</div>
</div>
""", unsafe_allow_html=True)
    mean_length = round(int(df['Daily Operated Length (Kms.)'].mean()))
    mean_fleet = round(int(df['RTC Fleet of Buses'].mean()))
    mean_depots = round(int(df['RTC Bus Depots'].mean()))
    actual_length = int(new_df['Daily Operated Length (Kms.)'].iloc[0])
    actual_fleet =  int(new_df['RTC Fleet of Buses'].iloc[0])
    actual_depots = int(new_df['RTC Bus Depots'].iloc[0])
    don, gra = st.columns(2, gap = 'medium')
    with don:
        st.markdown(f"""<div class = 'don-container'><div class = 'subheader'>Mean Distance in a day {mean_length} kms</div></div>""", unsafe_allow_html=True)
        st.plotly_chart(donut(actual_length, mean_length, 'Distance', '#ffffff'))
        st.markdown(f"""<div class = 'don-container'><div class = 'subheader'>Mean fleet {mean_fleet}</div></div>""", unsafe_allow_html=True)
        st.plotly_chart(donut(actual_fleet, mean_fleet, 'Fleet', '#ffffff'))
        st.markdown(f"""<div class = 'don-container'><div class = 'subheader'>Mean Depots {mean_depots}</div></div>""", unsafe_allow_html=True)
        st.plotly_chart(donut(actual_depots, mean_depots, 'Mean Depots', '#ffffff'))
    with gra:
        fig1 = px.bar(df, x = 'Districts', y = 'Daily Operated Length (Kms.)', title = 'District vs Operated Length daily')
        fig2 = px.bar(df, x = 'Districts', y = 'RTC Fleet of Buses', title = 'Districts vs Bus Fleet')
        fig3 = px.bar(df, x = 'Districts', y = 'RTC Bus Depots', title = 'Districts vs Bus Depots')
        fig1.add_hline(y = mean_length, line_dash = 'dash', line_color = 'red', annotation_text = 'mean length', annotation_position = 'top left')
        fig2.add_hline(y = mean_fleet, line_dash = 'dash', line_color = 'red', annotation_text = 'mean fleet', annotation_position = 'top left')
        fig3.add_hline(y = mean_depots, line_dash = 'dash', line_color= 'red', annotation_text = 'mean depots', annotation_position = 'top left')
        fig1.update_traces(marker_color = ['lightskyblue' if d == filter else 'lightgrey' for d in df['Districts']])
        fig2.update_traces(marker_color = ['lightskyblue' if d == filter else 'lightgrey' for d in df['Districts']])
        fig3.update_traces(marker_color = ['lightskyblue' if d == filter else 'lightgrey' for d in df['Districts']])
        st.plotly_chart(fig1, use_container_width=True)
        st.plotly_chart(fig2, use_container_width=True)
        st.plotly_chart(fig3, use_container_width=True)


