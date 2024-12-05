#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:43:17 2024

@author: xap
"""
import streamlit as st
import pandas as pd
import plotly.express as px


class Page2():
    def __init__(self)-> None:
        # df = functions.create_packet_dataframe(st.session_state['ps'].packets_param_list)
        # LAYING OUT THE TOP SECTION OF THE APP
        row1_1, row1_2 = st.columns((5, 5), gap = "large")

        with row1_1:
            fig_plotly = px.line(
            st.session_state['plog'].dataframe,
            x=st.session_state['plog'].dataframe.index,
            y=['sveglia_sx m', 'sveglia_dx m'],
            labels={'x': 'Data', 'value': 'Valori'},
            title="Mattina minima sx e dx",
            color_discrete_map={'sveglia_sx m': 'red', 'sveglia_dx m': 'blue'}
            )
            st.plotly_chart(fig_plotly) 

        with row1_2:
            fig_plotly = px.line(
            st.session_state['plog'].dataframe,
            x=st.session_state['plog'].dataframe.index,
            y=['sveglia_sx M', 'sveglia_dx M'],
            labels={'x': 'Data', 'value': 'Valori'},
            title="Mattina Massima sx e dx",
            color_discrete_map={'sveglia_sx M': 'red', 'sveglia_dx M': 'blue'}
            )
            st.plotly_chart(fig_plotly)  


  
