

import streamlit as st
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz

df = pd.read_csv('product_data.csv')

categories = [x for x in df['CATEGORY'].unique()]

cat1 = st.selectbox("Category", options=categories)

df2 = df[df['CATEGORY'] == cat1]

cat2 = st.selectbox("Subcategory", options=[x for x in df2['SUB_CATEGORY'].unique()])

df3 = df2[df2['SUB_CATEGORY'] == cat2]

text_input = st.text_input('Search Products')

df3['SCORE'] = np.zeros(len(df3))
df3.reset_index()

for i in range(len(df3)):
	df3['SCORE'].iloc[i] = fuzz.ratio(df3['DESCRIPTION'].iloc[i].upper(), text_input.upper())

df4 = df3.drop(columns=['UPC', 'MANUFACTURER', 'PRODUCT_SIZE'])

st.write(df4.sort_values(by='SCORE', ascending=False).head(10))
