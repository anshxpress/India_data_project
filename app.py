import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd

st.set_page_config('wide')
df = pd.read_csv('india.csv')

list_of_state = list(df['State'].unique())
list_of_state.insert(0, 'Over-All India')

st.sidebar.title('India Visualization')

selected_state = st.sidebar.selectbox('State-Box', list_of_state)
Primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
Secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))


plot = st.sidebar.button('plot Graph')

if plot:

    st.text('size represents primary parameter')
    st.text('color represents secondary parameter')
    if selected_state == 'Over-All India':

        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=Primary, color=Secondary, zoom=3,
                                mapbox_style="carto-positron",width=1200, height=700,hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=Primary, color=Secondary, zoom=6,
                                mapbox_style="carto-positron", width=1200, height=700, hover_data='District')
        st.plotly_chart(fig, use_container_width=True)
