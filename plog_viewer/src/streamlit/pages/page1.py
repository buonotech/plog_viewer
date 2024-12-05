#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:43:17 2024

@author: xap
"""
import streamlit as st
import pandas as pd

import os




class Page1():
    def __init__(self)-> None:
        
        # LAYING OUT THE TOP SECTION OF THE APP
        row1_1, row1_2= st.columns((3, 3), gap = "large")

        with row1_1:
            # TITLE    
            st.write("## PLog viewer")
            st.write("#")

        with row1_2:
            # st.write("#")
            uploaded_file = st.file_uploader("Choose a file")

  
        row2_1, row2_2= st.columns([10,1], gap = "large")
        with row2_1:
            if uploaded_file is not None:
            
                st.session_state['plog'].dataframe = pd.read_excel(uploaded_file, index_col=0)
                st.write(st.session_state['plog'].dataframe)

        # with row2_1:
        #     st.write("### Unwrapped Time Series")        
        #     if st.session_state.data_off == False:      
        #         with row2_2:
        #             fig_unwrapped_ts = figures.create_fig_unwrapped_ts(ps_id)
        #             st.plotly_chart(fig_unwrapped_ts, use_container_width=True)
    
        # row3_1, row3_2, row3_3= st.columns([1, 5, 0.6], gap = "large")
        # with row3_1:
        #     st.write("### Noise") 
        # with row3_2:
        #     if st.session_state.data_off == False: 
        #         fig_noise_ts = figures.create_fig_ts(st.session_state['ps'].get_n(), ps_id, "Noise", "black")
        #         st.plotly_chart(fig_noise_ts, use_container_width=True)
 
        # row4_1, row4_2, row4_3= st.columns([1, 5, 0.6], gap = "large")
        # with row4_1:
        #     st.write("### Phase Jumps") 
            
        # with row4_2:
        #     if st.session_state.data_off == False: 
        #         fig_ph_ts = figures.create_fig_ts(st.session_state['ps'].get_kd(), ps_id, "kd", 'red')
        #         st.plotly_chart(fig_ph_ts, use_container_width=True) 

        # row5_1, row5_2, row5_3= st.columns([1, 5, 0.6], gap = "large")
        # with row5_1:
        #     st.write("### Seasonality") 
        # if st.session_state.data_off == False:       
        #     with row5_2:
        #         fig_season_ts = figures.create_fig_ts(st.session_state['ps'].get_season(), ps_id, "seasonality", 'green')
        #         st.plotly_chart(fig_season_ts, use_container_width=True)

