import pandas as pd

SPEED = "generator_speed"
POWER = "power"
ANOMALY_SCORE = "anomaly_score"
ANOMALY = "anomaly"
TIME = "time"
LABEL = "label"
START_TIME = "startTime"
END_TIME = "endTime"




df_normal_label = pd.read_csv('~/Desktop/PHM/data_related/Blade-Icing/turbine15/15_normalInfo.csv')
df_failure_label = pd.read_csv('~/Desktop/PHM/data_related/Blade-Icing/turbine15/15_failureInfo.csv')

def test_the_order_of_time_stamp(df):
    last_end_time_stamp = ...
    for i, cur_row in df.iterrows():
        if i == 0:
            assert cur_row[START_TIME] < cur_row[END_TIME]
        else:
            assert last_end_time_stamp < cur_row[START_TIME] < cur_row[END_TIME]

        last_end_time_stamp = cur_row[END_TIME]



test_the_order_of_time_stamp(df_normal_label)
test_the_order_of_time_stamp(df_failure_label)


#Asset passed. Conclusion: the time stamps in maintainance dataset is ordered in time.