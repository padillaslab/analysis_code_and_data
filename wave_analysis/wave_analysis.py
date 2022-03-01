from io import StringIO
import math
from os import error
from tracemalloc import start
from turtle import color
from numpy import datetime64, iterable
import pandas as pd
import csv
from pandas.core.frame import DataFrame
from datetime import datetime
import matplotlib.pyplot as plt
from sympy import fft, ifft
import numpy.fft as np

# converts string to datetime
# params:
## str: str format datetime
## str: datetime format
# returns:
## datetime
def convert_str_datetime(str, str_format):
    date = datetime.datetime.strptime(str, str_format)
    return date

# converts string arr to datetime arr
# params:
## str[]: str array of format datetime
## str: datetime format
# returns:
## datetime arr
def convert_str_datetime_arr(str_arr, str_format):
    datetime_arr = []
    for str in str_arr:
        datetime_arr.append(convert_str_datetime(str, str_format))
    return datetime_arr

#bins data in arr in bin_len
def bin_data(arr, bin_len):
    if(len(arr)%bin_len != 0): print('Bin length is not valid')
    bin_arr = []
    temp_bin = 0
    ite = 1
    for value in arr:
        temp_bin += value
        if(ite%bin_len == 0):
            bin_arr.append(temp_bin/bin_len)
            temp_bin = 0
        ite += 1
    return bin_arr

def get_time_based_column(df, target_col, time_col, start_time, end_time):
    new_arr = []
    for index, row in df.iterrows():
        if(row[time_col]>=start_time and row[time_col]<=end_time):
            new_arr.append(row[target_col])
    return new_arr

def add_ave_column(df: DataFrame, col_arr, ave_col_name):
    ave_arr = []
    temp_total = 0
    for item in df.iterrows():
        for col in col_arr:
            temp_total += item[col]
        ave_arr.append(temp_total/len(col_arr))
        temp_total = 0
    df[ave_col_name] = ave_arr

pad_df = pd.read_excel("Aug26_sept7_forMB.xlsx")
## mark light and dark
# lc_array = []
# for index, row in df.iterrows():
#     if((row['Time'] > datetime(1,1,1,7,30,0).time()) & (row['Time'] < datetime(1,1,1,19,30,0).time())):
#         lc_array.append('l')
#     else:
#         lc_array.append('d')
# df['lc'] = lc_array

# ## mark experiment day
day_array = []
for index, row in pad_df.iterrows():
    if(row['Time'] < datetime(1,1,1,7,30,0).time()):
        day_array.append(row['Date'].dayofyear - 240)
    else:
        day_array.append(row['Date'].dayofyear - 239)
pad_df['ex.day'] = day_array

# ## filter baseline days
# base_df = df[((df['ex.day']>0) & (df['ex.day']<=5))]

# # filter ovexed days
# ovx_df = df[((df['ex.day']==0) & (df['Time']>datetime(1,1,1,7,30,0).time())) | ((df['ex.day']>0) & (df['ex.day']<5)) | ((df['ex.day']==5) & (df['Time']<datetime(1,1,1,7,30,0).time()))]

# # average temperatures for all female mice
# ave_arr = []
# for index, row in base_df.iterrows():
#     temp = (row['F1'] + row['F2'] + row['F3'] + row['F4']+ row['F5'] + row['F6'])/6
#     ave_arr.append(temp)
# base_df['ave'] = ave_arr

# # average day temperature
# day_ave_arr = []
# for min in range(1440):
#     day_ave_arr.append(0)
# day_df = base_df[(base_df['ex.day']==4)]
# min = 0
# for index, row in day_df.iterrows():
#     day_ave_arr[min] += row['F1']
#     min += 1 

##filter light and dark
# light_ave_arr = day_ave_arr[0:720]
# dark_ave_arr = day_ave_arr[720:1440]

# ##bin data
# la_bin = bin_data(light_ave_arr, 5)
# # da_bin = bin_data(dark_ave_arr, 5)

# for i in range(len(la_bin)):
#     la_bin[i] = round(la_bin[i],1)


df = pd.read_excel("Aug26_sept7_forMB.xlsx")
def get_filter_arr(mice, ex_day, start_min, end_min):
    filter_arr = []
    for index, row in pad_df.iterrows():
        if row["ex.day"] == ex_day and row['Time'].minute+row['Time'].hour*60>=start_min and row['Time'].minute+row['Time'].hour*60<end_min:
            filter_arr.append(row[mice])
    return filter_arr

female='F3'
array_1 = get_filter_arr(female, 6, 0, 1440)
bin_1 = bin_data(array_1, 5)
# array_2 = get_filter_arr(female, 6, 0, 1440)
# bin_2 = bin_data(array_2, 5)
plt.plot(bin_1, color="orange")
# plt.psd(bin_2)
plt.show()