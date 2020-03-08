# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 09:41:48 2020

@author: mukul
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns

df_C = pd.read_csv("C:/Users/mukul/Desktop/ML Sessions/Day6/candidate09.csv", delimiter = ',')
df_E = pd.read_csv("C:/Users/mukul/Desktop/ML Sessions/Day6/LS2009Electors.csv" , delimiter = ',')
df_C.shape
df_E.shape
df_C.columns
df_E.columns


x = list(df_C['Candidate_Sex'].value_counts().to_dict().keys() )
y = list(df_C['Candidate_Sex'].value_counts().to_dict().values() )

plt.bar(x, y)
plt.title('Male vs. Female')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

df_C['Candidate_Category']
df_C.columns
df_E.columns