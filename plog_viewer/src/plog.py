#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:33:35 2024

@author: xap
"""
import numpy as np
import pandas as pd



class InvalidDuration(Exception):
    pass


class PLog():
    def __init__(self):
        self.dataframe = pd.DataFrame()
