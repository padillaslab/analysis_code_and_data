from cmath import exp
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import analysis_function
import datetime

# nest_clb_df = pd.read_csv("622_nest_jan_14.csv", skiprows=7)
# cage_clb_df = pd.read_csv("622_cage_jan_14.csv", skiprows=7)

BI_df = pd.read_csv("PIR_output.csv")
BI_df['Timestamp'] = analysis_function.convert_str_datetime_arr(BI_df['Timestamp'], "%m/%d/%y %H:%M")
BI_df['Exp. Day'] = analysis_function.get_exp_day_arr(BI_df['Timestamp'], datetime.datetime(2022, 1, 8, 5, 0, 0))

# def get_day_arr_clb_output(df, exp_day, start_min):
#     day_arr = []
#     for index, row in df.iterrows():
#         if(row['Min / Day']>start_min):
#             day_arr.append(row[exp_day])
#     for index, row in df.iterrows():
#         if(row['Min / Day']<=start_min):
#             day_arr.append(row[exp_day+1])
#     return day_arr

# ## clb analysis
# for day in range(17,20):
#     print(day)
#     cage_data = get_day_arr_clb_output(cage_clb_df, day, 300)
#     nest_data = get_day_arr_clb_output(nest_clb_df, day, 300)
#     day_sum = 0
#     night_sum = 0
#     for count in cage_data[0:720]:
#         day_sum+=count
#     for count in cage_data[720:1440]:
#         night_sum+=count
#     print('Cage data:')
#     print('Day sum: ' + str(day_sum))
#     print('night sum: ' + str(night_sum))
    
#     day_sum = 0
#     night_sum = 0
#     for count in nest_data[0:720]:
#         day_sum+=count
#     for count in nest_data[720:1440]:
#         night_sum+=count
#     print('Nest data:')
#     print('Day sum: ' + str(day_sum))
#     print('night sum: ' + str(night_sum))
# plt.plot(get_day_arr_clb_output(cage_clb_df, 19, 300), color='green')
# plt.plot(get_day_arr_clb_output(nest_clb_df, 19, 300))
# plt.show()

## BI analysis
for psc in range(1,11):
    if (psc == 7 or psc == 9):
        continue
    psc_name = 'Count ' + str(psc)
    for day in range(1,4):
        print(psc_name)
        print(day)
        temp_data = analysis_function.get_day_col_arr(BI_df, day, psc_name, 'Exp. Day')
        day_sum = 0
        night_sum = 0
        for count in temp_data[0:720]:
            day_sum+=count
        for count in temp_data[720:1440]:
            night_sum+=count
        print('Day sum: ' + str(day_sum))
        print('night sum: ' + str(night_sum))
        plt.plot(temp_data, color='red')
        plt.show()