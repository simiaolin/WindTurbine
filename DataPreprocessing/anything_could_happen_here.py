from common.config_bladeicing import *
import pandas as pd

df_with_label = pd.read_csv(preprocessed_file)
# df_with_label.info()
df = df_with_label.loc[:, [TIMESTAMP,TURBINE, FAILURE]]
df = df[df[TURBINE] == "T21"]
df.info()


df2 = pd.read_csv(new_data_file_with_label)
df2.dropna(inplace=True)
df2 = df2.loc[:, [TIME, LABEL]]
df2.info()

cnt = 0
for i, currow in df2.iterrows():
    timestamp = currow[TIME]
    value_in_my_process = currow[LABEL]
    value_in_preprocess = df[df[TIMESTAMP] == timestamp].iloc[0][FAILURE]
    if value_in_my_process == -1:
        if value_in_preprocess != 1:
            cnt+=1
    elif value_in_my_process == 1:
        if value_in_preprocess != 0:
            cnt+=1
print(f'altogether {cnt} instances ')
# print(f'{len(df_with_label[df_with_label[TURBINE]== "T21"])}')
# df = pd.read_csv(new_data_file_with_label)
# df.info()
