from hashlib import new
from time import time
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame

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

# marks experiment days
# params:
## datetime_arr[]: array of datetime
## start_datetime
# returns:
## array of exp. days
def get_exp_day_arr(datetime_arr, start_datetime):
    exp_day_arr = []
    for datetime_temp in datetime_arr:
        exp_day = (datetime_temp - start_datetime).days + 1
        exp_day_arr.append(exp_day)
    return exp_day_arr

# filters array for desired exp. day and column
# params:
## df: dataframe
## int: exp_day
## string: target column name
## string: experiment day column name
# returns:
## array: filtered array for the desired psc and day
def get_day_col_arr(df, exp_day, col_name, exp_day_col):
    day_psc_arr = []
    for index, row in df.iterrows():
        if(row[exp_day_col] == exp_day):
            day_psc_arr.append(row[col_name])
    return day_psc_arr

## return sum of a column on a time filter basis
def sum_column_using_datetime(df, col_name, datetime_col, start_datetime, end_datetime, addition_column_arr):
    total = 0
    for index, row in df.iterrows():
        add_row = True
        if(-(row[datetime_col] >= start_datetime and row[datetime_col] <= end_datetime)):
            add_row = False
        for column in addition_column_arr:
            if(row[column[0]]!=column[1]):
                add_row = False
        if(add_row):
            total += row[col_name]        
    return total

## prints desired outliers for a column in a dataframe
def print_outliers(df, time_col, start_time, end_time, target_col, lower_limit, upper_limit):
    fil_df = df[(df[time_col]>start_time) & (df[time_col]<end_time)]
    outlier_num = 0
    for index, row in fil_df.iterrows():
        if(row[target_col]>upper_limit or row[target_col]<lower_limit):
            outlier_num += 1
            print(row[time_col])
            print(row[target_col])
    print('Number of Outliers: ' + str(outlier_num))

##fills the last 3-4 entries for a day of entries
def day_fill_in_bootleg_array(arr):
    last_entry = arr[len(arr)-1]
    for misses in range(1440-len(arr)):
        arr.append(last_entry)
    return arr

# converts string to datetime
# params:
## int[]: array to be binner
## int: bin length
# returns:
## int[]: binned array
def bin_arr(arr, bin_length):
    bin_arr = []
    bin_temp = 0
    cur_bin_len = 0
    for num in arr:
        cur_bin_len += 1
        bin_temp += num
        if(cur_bin_len==bin_length):
            bin_arr.append(bin_temp/bin_length)
            cur_bin_len = 0
            bin_temp = 0
    return bin_arr

## biodaq analysis
# biodaq_df = pd.read_excel('biodaq.xlsx', sheet_name='mihir')
# x_axis = []
# y_axis = []

# biodaq_df_day_28_psc_7 = biodaq_df[(biodaq_df['PSC']==7) & ((biodaq_df['Start']>=datetime.datetime(2021, 12, 29, 5, 0, 0)) & (biodaq_df['Start']<datetime.datetime(2021, 12, 30, 5, 0, 0)))]
# biodaq_df_day_28_psc_7.index = range(len(biodaq_df_day_28_psc_7.index))
# for index, row in biodaq_df_day_28_psc_7.iterrows():
#     x_axis.append(round((row['Start'] - datetime.datetime(2021, 12, 28, 5, 0, 0)-datetime.timedelta(1)).total_seconds() /60, 0))
#     temp = 0
#     if(row['Consumed Grams']>0):
#         temp = 1
#     y_axis.append(temp)

# plt.plot(x_axis, y_axis, 'ro')
# plt.show()