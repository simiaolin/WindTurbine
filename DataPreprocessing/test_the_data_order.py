import pandas as pd
from  common.config_bladeicing import  *
from datetime import datetime
df_normal_label = pd.read_csv(normal_info_file)
df_failure_label = pd.read_csv(failure_info_file)

def get_timestamp(str):
    return datetime.strptime(str, datatime_for_start_end_in_info_file)
def test_the_order_of_time_stamp(df):
    last_end_time_stamp = ...
    for i, cur_row in df.iterrows():
        if i == 0:
            assert get_timestamp(cur_row[START_TIME]) < get_timestamp(cur_row[END_TIME])
        else:

            assert last_end_time_stamp < get_timestamp(cur_row[START_TIME]) < get_timestamp(cur_row[END_TIME])

        last_end_time_stamp = get_timestamp(cur_row[END_TIME])



test_the_order_of_time_stamp(df_normal_label)
test_the_order_of_time_stamp(df_failure_label)


#Asset passed. Conclusion: the time stamps in maintainance dataset is ordered in time.