# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 20:15:44 2021

@author: Oscar P
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv('eur_cop.csv', index_col = 'Date', parse_dates=True)

df.Price.plot(figsize = (12,6))
plt.show()