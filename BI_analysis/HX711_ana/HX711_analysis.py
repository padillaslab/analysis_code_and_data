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

g_name = 'Weight ' + str(3)
w_name = 'Weight ' + str(4)
day = 3
print("Day " + str(day))
HX_data = analysis_function.get_day_col_arr(HX711_df, day, g_name, 'Exp. Day')
g_first_entry = HX_data[0]
for ite in range(len(HX_data)):
    HX_data[ite] = -(HX_data[ite]-g_first_entry)/10
HX_data = analysis_function.day_fill_in_bootleg_array(HX_data)
HX_data = analysis_function.bin_arr(HX_data, 60)
analysis_function.print_outliers(HX711_df, 'Timestamp', datetime.datetime(2022, 1, 7+day, 5, 0, 0), datetime.datetime(2022, 1, 8+day, 5, 0, 0), g_name, -50, -35)
plt.plot(HX_data)
plt.grid(True, color="grey", linewidth="1.4")
plt.show()