#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:43:17 2024

@author: xap
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff


class Page3():
    def __init__(self)-> None:
        # df = functions.create_packet_dataframe(st.session_state['ps'].packets_param_list)
        # LAYING OUT THE TOP SECTION OF THE APP
        
        row1_1, row1_2 = st.columns((5, 5), gap = "large")
        fixed_bin_size=10,
        with row1_1:
            if 'plog' in st.session_state and not st.session_state['plog'].dataframe.empty:
                df_cleaned = st.session_state['plog'].dataframe[['sveglia_sx m', 'sveglia_dx m']].dropna()
        
                # Ensure the cleaned DataFrame is not empty
                if not df_cleaned.empty:
                    # Melt the DataFrame to prepare for a grouped histogram
                    df_melted = df_cleaned.melt(var_name='Category', value_name='Value')
        
                    # Create a histogram
                    fig = px.histogram(
                        df_melted,
                        x='Value',
                        color='Category',  # Group by category (column names)
                        barmode='overlay',  # Overlay histograms
                        nbins=10,  # Adjust the number of bins
                        title="Distribution of sveglia_sx m and sveglia_dx m",
                        color_discrete_map={'sveglia_sx m': 'red', 'sveglia_dx m': 'blue'}

                    )
                    fig.update_layout(
                        xaxis_title="Value",
                        yaxis_title="Count",
                        bargap=0.1  # Reduce gap between bars for better visualization
                    )
                    st.plotly_chart(fig)
                else:
                    st.warning("The columns 'sveglia_sx M' and 'sveglia_dx M' contain no valid data.")
            

        with row1_2:
            if 'plog' in st.session_state and not st.session_state['plog'].dataframe.empty:
                df_cleaned = st.session_state['plog'].dataframe[['sveglia_sx M', 'sveglia_dx M']].dropna()
        
                # Ensure the cleaned DataFrame is not empty
                if not df_cleaned.empty:
                    # Melt the DataFrame to prepare for a grouped histogram
                    df_melted = df_cleaned.melt(var_name='Category', value_name='Value')
        
                    # Create a histogram
                    fig = px.histogram(
                        df_melted,
                        x='Value',
                        color='Category',  # Group by category (column names)
                        barmode='overlay',  # Overlay histograms
                        nbins=10,  # Adjust the number of bins
                        title="Distribution of sveglia_sx M and sveglia_dx M",
                        color_discrete_map={'sveglia_sx M': 'red', 'sveglia_dx M': 'blue'}
                    )
                    fig.update_layout(
                        xaxis_title="Value",
                        yaxis_title="Count",
                        bargap=0.1  # Reduce gap between bars for better visualization
                    )
                    st.plotly_chart(fig)
                else:
                    st.warning("The columns 'sveglia_sx M' and 'sveglia_dx M' contain no valid data.")
        
          
