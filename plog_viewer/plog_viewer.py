#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 22:44:13 2024

@author: xap
"""

import streamlit as st

from src.plog import PLog

import src.streamlit.pages.page1 as pg1
import src.streamlit.pages.page2 as pg2
import src.streamlit.pages.page3 as pg3
import src.streamlit.pages.page4 as pg4


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title= "Plog viewer", page_icon=":satellite:")
# Setting padding at the top
st.markdown("""<style> div.block-container{padding-top:2rem;}
            </style>""", unsafe_allow_html=True)

# Initialization
# Control flag to state the presence of data to be shown
# ps_number = 0
# if "initial_data_dir" not in st.session_state:
#     st.session_state['initial_data_dir'] = '/mnt/DATI_PC/AAA_DOTTORATO/LAVORI/SOFTWARE_MIEI/TS_simulator/PS_simulator_3.0/sPS_Collections' 
# if "data_off" not in st.session_state:
#     st.session_state['data_off'] = True
if "plog" not in st.session_state:
    st.session_state['plog'] = PLog() 

# Creation of synthetic packet dataframe

            
# LAYOUT SETTINGS

tab1, tab2, tab3, tab4 = st.tabs(["Database", "Timeseries", "Distributions", "Boxplot"])

with tab1:
    page1 = pg1.Page1()

with tab2:
    page2 = pg2.Page2()

with tab3:
    page3 = pg3.Page3()
    
with tab4:
    page4 = pg4.Page4()