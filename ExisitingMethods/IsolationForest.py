import pandas as pd
import seaborn as sns
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

df = pd.read_csv('~/Desktop/PHM/data_related/Blade-Icing/turbine15/15_data.csv')
# print(df.info())
# df.dropna()
SPEED = "generator_speed"
POWER = "power"
ANOMALY_SCORE = "anomaly_score"
ANOMALY = "anomaly"

anomaly_inputs = [SPEED, POWER]

model_IF = IsolationForest(contamination=0.06, random_state=42)
model_IF.fit(df[anomaly_inputs])
df[ANOMALY_SCORE] = model_IF.decision_function(df[anomaly_inputs])
df[ANOMALY] = model_IF.predict(df[anomaly_inputs])

df.loc[:, [SPEED, POWER, ANOMALY_SCORE, ANOMALY]]


def outlier_plot(data, outlier_method_name, x_var, y_var, xaxis_limits=[0, 1], yaxis_limits=[0, 1]):
    print(f'Outlier method: {outlier_method_name}')

    g = sns.FacetGrid(data, col='anomaly', height=4, hue='anomaly', hue_order=[1, -1])
    g.map(sns.scatterplot, x_var, y_var)
    g.set(xlim=xaxis_limits, ylim=yaxis_limits)
    axes = g.axes.flatten()
    axes[0].set_title(f'{len(data[data[ANOMALY] == -1])} points')
    axes[1].set_title(f'{len(data[data[ANOMALY] == 1])} points')
    return g


outlier_plot(df, "IF", SPEED, POWER, [-2, 2], [-1.5, 4])

#
#
palette = ['#ff7f0e', '#1f77b4']
sns.pairplot(df, vars=anomaly_inputs, hue=ANOMALY, palette=palette)
plt.show()
