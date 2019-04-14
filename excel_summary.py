#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import pandas as pd
import glob
import openpyxl


dir = ''
name_excel='Jan 13th Hotel no summary.xlsx'
os.chdir(dir)
os.chdir(dir)



#Delete the summary page before input the file
dfs = pd.read_excel(name_excel, sheetname=None, ignore_index=True)
#Merge all the sheets
df=pd.concat([df.assign(name=n) for n,df in dfs.items()])



df=df.reset_index(drop=True)



df = df [['Token','Date/Time','name','Bebot messages']]
df['Token']=df['Token'].fillna(method='ffill')
#Calculate the number of unique Token
n_user_hotel=df.groupby('name')['Token'].nunique().to_frame().sort_values(by='Token', ascending=False)
n_user=df['Token'].nunique()
n_user_hotel
n_user



#Calculate chat time
df['Date/Time']=pd.to_datetime(df['Date/Time'])



df['diff']=df.sort_values(['Token','Date/Time']).groupby('Token')['Date/Time'].diff()
df_diff=df[['Token','Date/Time','name','diff']]



#drop the rows when the chat stoped for 5 min
#df_dff=df[df['diff']< pd.to_timedelta('0 days 00:5:00')]



df_diff.loc[df_diff['diff']>pd.to_timedelta('0 days 00:5:00'), 'diff']=pd.to_timedelta('0 days 00:1:00')
type(df_diff)




duration_time=df_diff.groupby(['Token','name']).sum()


#Find the max duration time
max_duration=(duration_time[pd.to_timedelta(duration_time['diff'])==pd.to_timedelta(duration_time['diff']).max()])+pd.to_timedelta('0 days 00:1:00')




#Get the number of rate me
be_message=df[['name','Token','Bebot messages']].dropna()



rate=be_message[be_message['Bebot messages'].str.contains("rate me|写个好评|寫個好評")]['Bebot messages']#.count()
n_rate=rate.count()

print (__file__)
print('Excel Name --', name_excel)
print('Unique Users Each Hotel --', n_user_hotel)
print("Unique Users --", n_user)
print("Max_duration --", max_duration)
print("Review Requests Content--", rate)
print("Number of Review Requests --", n_rate)
