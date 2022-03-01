from random import random
from turtle import color
from numpy import datetime64
from scipy.fftpack import diff
import analysis_function
import pandas as pd
import datetime
import matplotlib.pyplot as plt

HX711_df = pd.read_csv('HX711_output.csv')
HX711_df['Timestamp'] = analysis_function.convert_str_datetime_arr(HX711_df['Timestamp'], "%m/%d/%Y %H:%M")
HX711_df['Exp. Day'] = analysis_function.get_exp_day_arr(HX711_df['Timestamp'], datetime.datetime(2022, 1, 8, 5, 0, 0))
##create fake data for water
water_data = []
light_slope = -0.1/720
last_point = 0
dark_slope = -1/720
current_min = 0
start_time = datetime.datetime(2022, 1, 8, 5, 0, 0)
time_arr = []

for min in range(720):
    last_point += (light_slope + (random()-0.5)/50)
    water_data.append(last_point)
    time_arr.append(start_time + datetime.timedelta(0,0,0,0,current_min,0,0))
    current_min+=1
for min in range(720):
    last_point += (dark_slope + (random()-0.5)/50)
    water_data.append(last_point)
    time_arr.append(start_time + datetime.timedelta(0,0,0,0,current_min,0,0))
    current_min+=1

for min in range(720):
    last_point += (light_slope + (random()-0.5)/50)
    water_data.append(last_point)
    time_arr.append(start_time + datetime.timedelta(0,0,0,0,current_min,0,0))
    current_min+=1
for min in range(720):
    last_point += (dark_slope + (random()-0.5)/50)
    water_data.append(last_point)
    time_arr.append(start_time + datetime.timedelta(0,0,0,0,current_min,0,0))
    current_min+=1

for min in range(720):
    last_point += (light_slope + (random()-0.5)/50)
    water_data.append(last_point)
    time_arr.append(start_time + datetime.timedelta(0,0,0,0,current_min,0,0))
    current_min+=1
for min in range(720):
    last_point += (dark_slope + (random()-0.5)/50)
    water_data.append(last_point)
    time_arr.append(start_time + datetime.timedelta(0,0,0,0,current_min,0,0))
    current_min+=1

water_df = pd.DataFrame({'Timestamp': time_arr, 'Weight 4': water_data})
water_df['Exp. Day'] = analysis_function.get_exp_day_arr(water_df['Timestamp'], datetime.datetime(2022, 1, 8, 5, 0, 0))

g_name = 'Weight ' + str(3)
w_name = 'Weight ' + str(4)
day = 3
print("Day " + str(day))
HX_data = analysis_function.get_day_col_arr(HX711_df, day, g_name, 'Exp. Day')
g_first_entry = HX_data[0]
for ite in range(len(HX_data)):
    HX_data[ite] = (HX_data[ite]-g_first_entry)/10
HX_data = analysis_function.day_fill_in_bootleg_array(HX_data)
HX_data = analysis_function.bin_arr(HX_data, 60)
analysis_function.print_outliers(HX711_df, 'Timestamp', datetime.datetime(2022, 1, 7+day, 5, 0, 0), datetime.datetime(2022, 1, 8+day, 5, 0, 0), g_name, -50, -35)
water_data = analysis_function.get_day_col_arr(water_df, day, w_name, 'Exp. Day')
w_first_entry = water_data[0]
for ite in range(len(water_data)):
    water_data[ite] = (water_data[ite]-w_first_entry)
water_data = analysis_function.bin_arr(water_data, 60)
plt.plot(HX_data)
plt.plot(water_data, color='red')
plt.show()