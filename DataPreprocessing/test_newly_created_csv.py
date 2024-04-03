import pandas as pd

data = pd.read_csv("~/Desktop/PHM/data_related/Blade-Icing/turbine15/15_data_with_label.csv", chunksize=10000)
df = pd.concat(data)
df.info()
df
