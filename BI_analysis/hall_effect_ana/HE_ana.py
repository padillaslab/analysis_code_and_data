import csv
from itertools import count
from sqlite3 import Timestamp
from typing import final
import pandas as pd
import analysis_function
import datetime

HE_df = pd.read_csv("HE_output.csv")
HE_df['Timestamp'] = analysis_function.convert_str_datetime_arr(HE_df['Timestamp'], "%m/%d/%y %H:%M")
HE_df['Exp. Day'] = analysis_function.get_exp_day_arr(HE_df['Timestamp'], datetime.datetime(2022, 1, 17, 5, 0, 0))


count_1 = []
for day in range(1, 5):
    count_temp = []
    day_df = HE_df[HE_df['Exp. Day']==day]
    cur_time = None
    temp = 0
    for index, row in day_df.iterrows():
        if cur_time == None:
            cur_time = row['Timestamp']
        elif cur_time == row['Timestamp']:
            temp+=row['Count 1']
        elif row['Timestamp'] != cur_time:
            cur_time=row['Timestamp']
            count_temp.append(temp)
            temp=0
    count_1 = count_1 + analysis_function.day_fill_in_bootleg_array(count_temp)
    
count_1 = analysis_function.bin_arr(count_1, 5)
for ite in range(len(count_1)):
    count_1[ite]=[count_1[ite]]

count_1 = [[],[],[],[],[],[],[]] + count_1

print(len(count_1))

with open("hall_effect_clb.csv", 'w', newline="") as f:
    write = csv.writer(f)
    write.writerows(count_1)