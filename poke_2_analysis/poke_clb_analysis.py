from os import error
from numpy import iterable
import pandas as pd
import csv
from pandas.core.frame import DataFrame
import datetime
import analysis_function
import matplotlib.pyplot as plt

poke_2_df = pd.read_csv('poke_2_output.csv')
poke_2_df['Time Stamp'] = analysis_function.convert_str_datetime_arr(poke_2_df['Time Stamp'], "%Y-%m-%d %H:%M:%S.%f")
poke_2_df['Exp. Day'] = analysis_function.get_exp_day_arr(poke_2_df['Time Stamp'], datetime.datetime(2021, 12, 28, 5, 0, 0))
biodaq_df = pd.read_excel('Mihirs_bullshit.xlsx', sheet_name='PSC by period', skiprows=8)
biodaq_df['Period Start'] = analysis_function.convert_str_datetime_arr(biodaq_df['Period Start'], "%m/%d/%Y %H:%M:%S")

clb_arr = [[],[],[],[],[],[],[]]
psc = 3
cs_name = 'CS ' + str(psc)
for day in range(1,6):
    cs_data = poke_2_df[poke_2_df['Exp. Day'] == day]
    cs_data = analysis_function.cs_activity_identifier(cs_data, 'Time Stamp', (datetime.datetime(2021, 12, 27, 5, 0, 0) + datetime.timedelta(days=day)), cs_name)
    cs_data.append(0)
    cs_data.append(0)
    cs_data.append(0)
    biodaq_data = biodaq_df[((biodaq_df['Period Start']>(datetime.datetime(2021, 12, 27, 5, 0, 0) + datetime.timedelta(days=day))) & (biodaq_df['Period Start']<=(datetime.datetime(2021, 12, 27, 5, 0, 0) + datetime.timedelta(days=(day+1)))) & (biodaq_df['PSC']==(psc+7)))]
    for point in cs_data:
        clb_arr.append([point])
    for index, row in biodaq_data.iterrows():
        clb_arr.append([row['Bouts']])

new_df = pd.DataFrame(clb_arr)
new_df.to_csv("poke_psc_10.csv", header=False, index=False)
