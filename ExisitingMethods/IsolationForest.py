import pandas as pd
import seaborn as sns
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
from common.config_bladeicing import *


def prepare_df(file):
    df = pd.read_csv(file)
    df.dropna(inplace=True)
    df.info()

    model_IF = IsolationForest(contamination=0.06, random_state=42)
    model_IF.fit(df[anomaly_inputs])
    df[ANOMALY_SCORE] = model_IF.decision_function(df[anomaly_inputs])
    df[ANOMALY] = model_IF.predict(df[anomaly_inputs])
    return df

def outlier_plot(data, label_column, x_var, y_var, xaxis_limits=[-1, 1], yaxis_limits=[-1, 1]):
    # print(f'Outlier method: {outlier_method_name}')
    g = sns.FacetGrid(data, col=LABEL, hue=label_column, hue_order=[-1, 1], palette=palette)
    g.map(sns.scatterplot, x_var, y_var, s=10)
    g.set(xlim=xaxis_limits, ylim=yaxis_limits)
                     # axes = g.axes.flatten()
    # axes[0].set_title(f'{len(data[data[label_column] == -1])} points')
    # axes[1].set_title(f'{len(data[data[label_column] == 1])} points')
    g.add_legend()
    return g


def visualize(df):
    outlier_plot(df, ANOMALY, SPEED, POWER, [-3, 6], [-1.5, 3])
    outlier_plot(df, LABEL, SPEED, POWER, [-3,6], [ -1.5, 3])
    # outlier_plot(df, LABEL, SPEED, POWER, [-3, 6], [-1.5, 3])

    sns.pairplot(df, vars=anomaly_inputs, hue=ANOMALY, palette=palette, size=10)
    sns.pairplot(df, vars=anomaly_inputs, hue=LABEL, palette=palette, size=10)
    plt.show()
def print_mislabel(df):
    print(f'Altogether there are{len(df)} instances')
    print(f'{len(df[df[LABEL] == df[ANOMALY]])} instances correctly labelled')
    print(f'{len(df[(df[LABEL] == 1) & (df[ANOMALY] == -1)])} anomalies are wrongly classified')
    print(f'{len(df[(df[LABEL] == -1) & (df[ANOMALY] == 1)])} normal instances are classified as anomalies')


if __name__ == '__main__':
    df = prepare_df(new_data_file_with_label)
    visualize(df)
    print_mislabel(df)