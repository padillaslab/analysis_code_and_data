from xml.dom import xmlbuilder
import analysis_function
import pandas as pd
import datetime
import matplotlib.pyplot as plt

# poke sensor analysis
poke_2_df = pd.read_csv('poke_2_output.csv')
poke_2_df['Time Stamp'] = analysis_function.convert_str_datetime_arr(poke_2_df['Time Stamp'], "%Y-%m-%d %H:%M:%S.%f")
poke_2_df['Exp. Day'] = analysis_function.get_exp_day_arr(poke_2_df['Time Stamp'], datetime.datetime(2021, 12, 28, 5, 0, 0))

biodaq_df = pd.read_excel('poke_2_test_biodaq.xlsx', sheet_name='mihir')

# def cs_activity_identifies(cs_data, time_stamp_col, exp_day, target_col):
#     for index, row in cs_data:


for psc in range(4):
    cs_name = 'CS ' + str(psc)
    for day in range(1, 6):
        biodaq_df_filtered = biodaq_df[(biodaq_df['PSC']==(7+psc)) & ((biodaq_df['Start']>=datetime.datetime(2021, 12, 28, 5, 0, 0)+datetime.timedelta(day-1)) & (biodaq_df['Start']<datetime.datetime(2021, 12, 29, 5, 0, 0)+datetime.timedelta(day-1)))]
        biodaq_df_filtered = biodaq_df_filtered.reset_index(drop=True)
        x_axis = []
        y_axis = []
        for index, row in biodaq_df_filtered.iterrows():
            x_axis.append(round(((row['Start'] - datetime.datetime(2021, 12, 28, 5, 0, 0))-datetime.timedelta(day-1)).total_seconds() /60, 0))
            temp = 1
            y_axis.append(temp)
        print("PSC: " + str(psc))
        print("Day: " + str(day))
        cs_data_1 = analysis_function.get_day_col_arr(poke_2_df, day, cs_name, 'Exp. Day')
        cs_data_1 = analysis_function.day_fill_in_bootleg_array(cs_data_1)
        plt.plot(cs_data_1)
        plt.plot(x_axis, y_axis, 'ro', markersize=5)
        cs_data = poke_2_df[poke_2_df['Exp. Day'] == day]
        cs_data = cs_activity_identifier(cs_data, 'Time Stamp', (datetime.datetime(2021, 12, 27, 5, 0, 0) + datetime.timedelta(days=day)), cs_name)
        plt.eventplot(cs_data, linewidth=0.75, linelengths=1, colors='C1', lineoffsets=0.5)
        plt.eventplot(x_axis, linewidth=0.75, linelengths=1, colors='C0', lineoffsets=1.5)
        plt.show()