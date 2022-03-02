import pandas as pd
import analysis_function
import datetime
import matplotlib.pyplot as plt

env_df = pd.read_csv("env_output.csv")

env_df['Timestamp'] = analysis_function.convert_str_datetime_arr(env_df['Timestamp'], "%m/%d/%y %H:%M")
env_df['Exp. Day'] = analysis_function.get_exp_day_arr(env_df['Timestamp'], datetime.datetime(2022, 1, 8, 5, 0, 0))

print(env_df)

final_arr = []
exp_day = 1
day_df = env_df[env_df['Exp. Day']==exp_day]

for index, row in day_df.iterrows():
    final_arr.append(row['Humidity'])

plt.plot(final_arr)
plt.show()