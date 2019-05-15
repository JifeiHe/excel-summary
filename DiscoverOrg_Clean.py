#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import pandas as pd
import glob
import openpyxl
import csv


dir = '/Users/jifeihe/Desktop/China_Telecom/DiscoverOrg'
os.chdir(dir)
os.chdir(dir)

name_excel='DiscoverOrg_PERSON_152498_20190501133358.csv'
conditions ='Filter.xlsx'
#Read states name list
dfs = pd.read_excel(conditions, ignore_index=True)

os.chdir(dir)
os.chdir(dir)

df=pd.read_csv(name_excel)
dfs['States Name']

#df=df[~df['Company Email Domain'].str.contains(".org|.edu|.gov")]
#df=df[~df['Company Primary Industry'].str.contains("Insurance|Banking|Hospitals|Health|Energy",na=False)]

#Drop rows without email
df=df[pd.notnull(df['Employee Work Email'])]

df=df[~df['Company Secondary Industries'].str.contains("Insurance|Banking|Hospitals|Health|Energy",na=False)]

df=df[~df['Company Email Domain'].str.contains('|'.join(dfs['Email'].dropna()))]
df.shape[0]

df=df[~df['Company Primary Industry'].str.contains('|'.join(dfs['Company Primary Industry'].dropna()))]
df.shape[0]

df=df[~df['Company Name'].str.contains('|'.join(dfs['States Name']))]
df.shape[0]

df=df[~df['Company Name'].str.contains('|'.join(dfs['Canada Name'].dropna()))]
df.shape[0]

df=df[~df['Employee Title'].str.contains('|'.join(dfs['Title'].dropna()))]
df.shape[0]

df=df[~df['Company Name'].str.contains('|'.join(dfs['Company Name'].dropna()))]

df.to_excel("outputs3.xlsx",index=False)
