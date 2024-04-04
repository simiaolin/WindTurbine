import pandas as pd
from common.config_bladeicing import *
from datetime import datetime

data = pd.read_csv(data_file, chunksize=10000)
df = pd.concat(data)
df.memory_usage(index=False, deep=True)
df = df[[TIME, SPEED, POWER]]
df.memory_usage(index=False, deep=True)

df_normal_label = pd.read_csv(normal_info_file)
df_failure_label = pd.read_csv(failure_info_file)

def  get_time_stamp(str):
    return datetime.strptime(str, datetime_format)

def get_time_stamp_for_start_and_end(str):
    return datetime.strptime(str, datatime_for_start_end_in_info_file)
def get_label(current_time_stamp):
    flag_step_out_the_last_boundary = False
    for _, normal_period in df_normal_label.iterrows():
        if get_time_stamp(current_time_stamp) < get_time_stamp_for_start_and_end(normal_period[START_TIME]):
            if flag_step_out_the_last_boundary:
                break
            else:
                continue
        else:
            if get_time_stamp(current_time_stamp) <= get_time_stamp_for_start_and_end(normal_period[END_TIME]):
                return +1 #inlier
            else:
                flag_step_out_the_last_boundary  = True
                continue

    flag_step_out_the_last_boundary = False
    for _, failure_period in df_failure_label.iterrows():
        if get_time_stamp(current_time_stamp) < get_time_stamp_for_start_and_end(failure_period[START_TIME]):
            if flag_step_out_the_last_boundary:
                break
            else:
                continue
        else:
            if get_time_stamp(current_time_stamp) <= get_time_stamp_for_start_and_end(failure_period[END_TIME]):
                return -1 #outlier
            else:
                flag_step_out_the_last_boundary = True
                continue

    return float('nan')

df[LABEL] = df[TIME].apply(get_label)
df.memory_usage(index=False, deep=True)
df.to_csv(new_data_file_with_label)
df.info()