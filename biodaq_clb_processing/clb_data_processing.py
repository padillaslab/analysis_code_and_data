from os import error
from numpy import iterable
import pandas as pd
import csv
from pandas.core.frame import DataFrame

#biodaq Info
biodaq_address = input("Enter Biodaq Filename: ")
biodaq_attribute = input("Biodaq Tracking Attribute: ")
biodaq_start_day = int(input("Biodaq Start Day: "))
biodaq_end_day = int(input("Biodaq End Day: "))
biodaq_start_end_min = int(input("Biodaq Start and End Min: "))
biodaq_psc = int(input("Biodaq PSC number: "))

#clocklab info
clocklab_address = input("Enter Clocklab Filename: ")
clocklab_start_day = int(input("Clocklab Start Day: "))
clocklab_end_day = int(input("Clocklab End Day: "))
clocklab_start_end_min = int(input("Clocklab Start and End Min: "))

#bin info
bin_length = int(input("Enter bin length in mins: "))

#result file info
new_clocklab_file_name = input("Enter the name of output CSV file: ")


biodaq_df = pd.read_excel(biodaq_address, sheet_name="PSC by period", skiprows=8)
clocklab_df = pd.read_csv(clocklab_address, skiprows=7)
new_array = [[],[],[],[],[],[],[]]

if(clocklab_end_day - clocklab_start_day != biodaq_end_day - biodaq_start_day): 
    raise Exception("Different number of days in Clocklab and Biodaq")

for day in range(clocklab_end_day-clocklab_start_day):
    minute_range_day_start = range(clocklab_start_end_min, 1440)
    minute_range_day_end = range(0, clocklab_start_end_min)

    #bin and add clocklab data
    iteration_count = 0
    iteration_total = 0
    for min in minute_range_day_start:
        temp_day = clocklab_df.columns[clocklab_start_day + day]
        iteration_count += 1
        iteration_total += clocklab_df[temp_day][min]
        if(iteration_count == bin_length):
            new_array.append([iteration_total/bin_length])
            iteration_count = 0
            iteration_total = 0
    iteration_count = 0
    iteration_total = 0
    for min in minute_range_day_end:
        temp_day = clocklab_df.columns[clocklab_start_day + day + 1]
        iteration_count += 1
        iteration_total += clocklab_df[temp_day][min]
        if(iteration_count == bin_length):
            new_array.append([iteration_total/bin_length])
            iteration_count = 0
            iteration_total = 0

    #bin and add clocklab data/
    filtered = biodaq_df[(biodaq_df["PSC"]==biodaq_psc) & (((biodaq_df["Exp. day"]==biodaq_start_day+day) & (biodaq_df["Period"]>biodaq_start_end_min)) | ((biodaq_df["Exp. day"]==biodaq_start_day+day+1) & (biodaq_df["Period"]<=biodaq_start_end_min)))]
    iteration_count = 0
    iteration_total = 0
    for index, row in filtered.iterrows():
        iteration_count += 1
        iteration_total += row[biodaq_attribute]
        if(iteration_count == bin_length):
            new_array.append([iteration_total/bin_length])
            iteration_count = 0
            iteration_total = 0
    new_array.append([0])

new_df = pd.DataFrame(new_array)
new_df.to_csv(new_clocklab_file_name, header=False, index=False)