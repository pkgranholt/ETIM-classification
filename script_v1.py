# -*- coding: utf-8 -*-

# Import packages
import matplotlib.pyplot as plt
import os
import pandas as pd
# import seaborn as sns

# Check/set wd
os.getcwd()

# Read file
df = pd.read_csv('Resultat.csv', sep=';')

# Set the product number as index
df = df.set_index('ProductNumber')

# Only keep the necessary columns for the project and change the column names
df = df[['ETIM klasse','Teknisk beskrivelse']]
df.columns = ['ETIM_class','Technical_description']
df['Elnr_group'] = df.index.astype(str).str[0:2]
df = df[['Elnr_group','ETIM_class','Technical_description']]

df.describe()

# How many of each ETIM-class are there within each elnr group?
ETIM_counts = df['ETIM_class'].value_counts()
Elnr_counts = df['Elnr_group'].value_counts()

grouped = pd.DataFrame(df.groupby(['Elnr_group', 'ETIM_class']).size())
grouped.columns = ['counts']

grouped = grouped.sort_values(['counts'],ascending=False).sort_index(axis=0,
                             level='Elnr_group', ascending=True,
                             sort_remaining=False)
grouped


# Visualisations
grouped.plot(kind='bar')


plt.plot(ETIM_counts.value_counts(), 1814)
plt.hist(ETIM_counts, 1814)
plt.plot(Elnr_counts)

