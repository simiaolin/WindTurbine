import pandas as pd
import seaborn as sns
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

SPEED = "generator_speed"
POWER = "power"
ANOMALY_SCORE = "anomaly_score"
ANOMALY = "anomaly"
TIME = "time"
LABEL = "label"
START_TIME = "startTime"
END_TIME = "endTime"



data = pd.read_csv('~/Desktop/PHM/data_related/Blade-Icing/turbine15/15_data.csv',chunksize=10000)
df = pd.concat(data)
df.memory_usage(index=False, deep=True)
df = df[[TIME, SPEED, POWER]]
df.memory_usage(index=False, deep=True)

df_normal_label = pd.read_csv('~/Desktop/PHM/data_related/Blade-Icing/turbine15/15_normalInfo.csv')
df_failure_label = pd.read_csv('~/Desktop/PHM/data_related/Blade-Icing/turbine15/15_failureInfo.csv')
# df.info()
# df_normal_label.info()
# df_failure_label.info()
# df.dropna()


def get_label(current_time_stamp):
    flag_step_out_the_last_boundary = False
    for _, normal_period in df_normal_label.iterrows():
        if current_time_stamp < normal_period[START_TIME]:
            if flag_step_out_the_last_boundary:
                break
            else:
                continue
        else:
            if current_time_stamp <= normal_period[END_TIME]:
                return 1
            else:
                flag_step_out_the_last_boundary  = True
                continue

    flag_step_out_the_last_boundary = False
    for _, failure_period in df_failure_label.iterrows():
        if current_time_stamp < failure_period[START_TIME]:
            if flag_step_out_the_last_boundary:
                break
            else:
                continue
        else:
            if current_time_stamp <= failure_period[END_TIME]:
                return -1
            else:
                flag_step_out_the_last_boundary = True
                continue

    return float('nan')

df[LABEL] = df[TIME].apply(get_label)
df.memory_usage(index=False, deep=True)
df.to_csv('~/Desktop/PHM/data_related/Blade-Icing/turbine15/15_data_with_label.csv')