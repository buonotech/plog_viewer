#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:43:17 2024

@author: xap
"""
import streamlit as st
import pandas as pd
import plotly.express as px


class Page4():
    def __init__(self)-> None:
        # df = functions.create_packet_dataframe(st.session_state['ps'].packets_param_list)
        # LAYING OUT THE TOP SECTION OF THE APP
        
        row1_1, row1_2 = st.columns((5, 5), gap = "large")
        with row1_1:
            if 'plog' in st.session_state and not st.session_state['plog'].dataframe.empty:
                df_cleaned2 = st.session_state['plog'].dataframe[['sveglia_sx m', 'sveglia_dx m']].dropna()
    
                # Melt the DataFrame to prepare for a grouped boxplot
                df_melted2 = df_cleaned2.melt(var_name='Category', value_name='Value')
    
                # Define custom colors
                color_map = {'sveglia_sx m': 'red', 'sveglia_dx m': 'blue'}
    
                # Create a boxplot
                fig = px.box(
                    df_melted2,
                    x='Category',  # Group by category (column names)
                    y='Value',  # Values for the boxplot
                    color='Category',  # Use the same grouping for color
                    color_discrete_map=color_map,  # Custom colors
                    title="Boxplot of sveglia_sx m and sveglia_dx m"
                )
                fig.update_layout(
                    xaxis_title="Category",
                    yaxis_title="Value",
                    boxmode='group'  # Group the boxplots
                )
                st.plotly_chart(fig)            

        with row1_2:
            if 'plog' in st.session_state and not st.session_state['plog'].dataframe.empty:
                df_cleaned2 = st.session_state['plog'].dataframe[['sveglia_sx M', 'sveglia_dx M']].dropna()
    
                # Melt the DataFrame to prepare for a grouped boxplot
                df_melted2 = df_cleaned2.melt(var_name='Category', value_name='Value')
    
                # Define custom colors
                color_map = {'sveglia_sx M': 'red', 'sveglia_dx M': 'blue'}
    
                # Create a boxplot
                fig = px.box(
                    df_melted2,
                    x='Category',  # Group by category (column names)
                    y='Value',  # Values for the boxplot
                    color='Category',  # Use the same grouping for color
                    color_discrete_map=color_map,  # Custom colors
                    title="Boxplot of sveglia_sx M and sveglia_dx M"
                )
                fig.update_layout(
                    xaxis_title="Category",
                    yaxis_title="Value",
                    boxmode='group'  # Group the boxplots
                )
                st.plotly_chart(fig)
                
