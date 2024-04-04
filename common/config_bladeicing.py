SPEED = "generator_speed"
POWER = "power"
ANOMALY_SCORE = "anomaly_score"
ANOMALY = "anomaly"
TIME = "time"
LABEL = "label"
TURBINE = "turbine"
FAILURE = "failure"
TIMESTAMP = "timestamp"
START_TIME = "startTime"
END_TIME = "endTime"
TIMESTAMP_FORMAT = ""
FOLDER_NAME = "~/Desktop/PHM/data_related/Blade-Icing/"
WIND_TURBINE_ID = 21
palette = ['red', 'green']
anomaly_inputs = [SPEED, POWER]
datetime_format = "%Y-%m-%d %H:%M:%S"
datetime_format_short = "%d/%m/%Y %H:%M"
datatime_for_start_end_in_info_file = datetime_format if WIND_TURBINE_ID == 15 else datetime_format_short
data_file = f'{FOLDER_NAME}turbine{WIND_TURBINE_ID}/{WIND_TURBINE_ID}_data.csv'
normal_info_file = f'{FOLDER_NAME}turbine{WIND_TURBINE_ID}/{WIND_TURBINE_ID}_normalInfo.csv'
failure_info_file = f'{FOLDER_NAME}turbine{WIND_TURBINE_ID}/{WIND_TURBINE_ID}_failureInfo.csv'
new_data_file_with_label = f'{FOLDER_NAME}turbine{WIND_TURBINE_ID}/{WIND_TURBINE_ID}_data_with_label.csv'
preprocessed_file = f'{FOLDER_NAME}Blade_icing_processed.csv'







