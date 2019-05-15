#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import pandas as pd
import glob
import openpyxl
import csv


name_file='Company_Enhance_Techs.csv'
df=pd.read_csv(name_file,encoding = "ISO-8859-1")

print (df.shape[0])
print (df.shape[1])

df["Web Analytics"].head()

def tidy_split(df, column, sep='|', keep=False):
    """
    Split the values of a column and expand so the new DataFrame has one split
    value per row. Filters rows where the column is missing.

    Params
    ------
    df : pandas.DataFrame
        dataframe with the column to split and expand
    column : str
        the column to split and expand
    sep : str
        the string used to split the column's values
    keep : bool
        whether to retain the presplit value as it's own row

    Returns
    -------
    pandas.DataFrame
        Returns a dataframe with the same columns as `df`.
    """
    indexes = list()
    new_values = list()
    df = df.dropna(subset=[column])
    for i, presplit in enumerate(df[column].astype(str)):
        values = presplit.split(sep)
        if keep and len(values) > 1:
            indexes.append(i)
            new_values.append(presplit)
        for value in values:
            indexes.append(i)
            new_values.append(value.lstrip()) #delete space
    new_df = df.iloc[indexes, :].copy()
    new_df[column] = new_values
    df_unique = new_df[column].unique()
    #new_df[column].to_excel("split.xlsx",index=False)
    return df_unique

dff=df.iloc[:,33:]
dff.head()

techs = dff.columns.values.tolist()

tech_df=pd.DataFrame()
for i, value in enumerate (techs):
    tech_df=pd.concat([tech_df,pd.Series(tidy_split(df, value, sep=',')).dropna()],axis=1,ignore_index=True)

tech_df.columns= dff.columns
tech_df.to_excel("tech_summary7.xlsx",index=False)
