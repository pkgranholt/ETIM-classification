# -*- coding: utf-8 -*-

# Import packages
import os
import pandas as pd
import matplotlib.pyplot as plt

# Check/set wd
os.getcwd()

# Read file
df = pd.read_csv('Resultat.csv', sep=';')

# Some descriptive attributes
print(df.head())
print(df.columns)
print(df.info())

# Set the product number as index
df = df.set_index('ProductNumber')
df.head()


print(df['Antall avvisninger'].value_counts(dropna=False))
print(df.iloc[:,1].value_counts(dropna=False))

df.count()

    
# Does not work
useless = df.count() == 0
print(df[useless])
df[useless == True].count()
df[useless]

# How to identify columns with all null values?
df['D-Pak GS1 128'].isnull().sum() == 238049