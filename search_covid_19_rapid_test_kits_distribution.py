# -*- coding: utf-8 -*-
"""search COVID-19 rapid test kits distribution .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zFC9369aZ2BMxKF4oN2zl2TCj63TC8wQ

[csv data](https://od.cdc.gov.tw/eic/covid19/covid19_free_rapid_antigen_test_clinics.csv)
"""

import pandas as pd
df = pd.read_csv("https://od.cdc.gov.tw/eic/covid19/covid19_free_rapid_antigen_test_clinics.csv")
df.drop(columns=['序號','Long','Lat'], inplace=True)

df.tail()

#main

while True:
  s = str(input("請輸入縣市別(輸入0結束):"))
  if s=="0":break

  filt = (df['縣市別'] == s)
  if len(df.loc[filt])==0: print("無資料")
  else: 
     a = df.loc[filt,['鄉鎮市區別', '診所名稱', '診所地址', '診所電話']]
     new_data=[]
     temp=[]
     for d in str(a).split('\n'):
       dd = d.split(" ")
       for ddd in dd:
         if ddd!="":temp.append(ddd)
       new_data.append(temp)
       temp=[]
     print(new_data[0][0],new_data[0][1],new_data[0][2],new_data[0][3])  
     print()
     for i in range(1,len(new_data)):
       print(new_data[i][1],new_data[i][2],new_data[i][3],new_data[i][4])  
       print()