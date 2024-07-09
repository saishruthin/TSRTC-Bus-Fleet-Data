import streamlit as st
import plotly.graph_objects as go
def donut(actual_value, mean_value, title, color):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = actual_value,
        title = {'text': f"{title}<br>{mean_value}", 'font': {'size': 15}},
        delta = {'reference': mean_value, 'relative': True, 'position': "top"},
        gauge = {
            'axis': {'range': [0, mean_value*2], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': color},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, mean_value], 'color': 'lightgrey'},
                {'range': [mean_value, mean_value*2], 'color': "grey"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': mean_value
            }
        }
    ))
    fig.update_layout(
        margin = dict(t=20, b=20, l=20, r=20),
        height = 250
    )
    return fig
