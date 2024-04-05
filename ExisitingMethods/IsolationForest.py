import pandas as pd
import seaborn as sns
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
from common.config_bladeicing import *


def prepare_df(file, usePreprocessed=False):
    if usePreprocessed:
        data = pd.read_csv(preprocessed_file, chunksize=10000)
        df = pd.concat(data)
        df = df.loc[:, [TIMESTAMP, SPEED, power, FAILURE]]
        df.info()
    else:
        df = pd.read_csv(file)
        df.dropna(inplace=True)
        df.info()
    return df

def prepare_df_preprocessed(preprocessed_file):
    data = pd.read_csv(preprocessed_file, chunksize=10000)
    df = pd.concat(data)
    df = df.loc[:, [TIME]]


def train_if(df):
    model_IF = IsolationForest(contamination=0.06, random_state=42)
    model_IF.fit(df[anomaly_inputs])
    df[ANOMALY_SCORE] = model_IF.decision_function(df[anomaly_inputs])
    df[ANOMALY] = model_IF.predict(df[anomaly_inputs])
    return df

def outlier_plot(data, hue_column, x_var, y_var, xaxis_limits=[-1, 1], yaxis_limits=[-1, 1]):
    # print(f'Outlier method: {outlier_method_name}')
    g = sns.FacetGrid(data, col=label_column, hue=hue_column, hue_order=hue_order, palette=palette)
    g.map(sns.scatterplot, x_var, y_var, s=10)
    g.set(xlim=xaxis_limits, ylim=yaxis_limits)
                     # axes = g.axes.flatten()
    # axes[0].set_title(f'{len(data[data[label_column] == -1])} points')
    # axes[1].set_title(f'{len(data[data[label_column] == 1])} points')
    g.add_legend()
    return g


def visualize(df):
    outlier_plot(df, ANOMALY, SPEED, power, [-3, 6], [-1.5, 3])
    outlier_plot(df, label_column, SPEED, power, [-3,6], [ -1.5, 3])

    sns.pairplot(df, vars=anomaly_inputs, hue=ANOMALY, palette=palette, size=10)
    sns.pairplot(df, vars=anomaly_inputs, hue=label_column, palette=palette, size=10)
    plt.show()
def print_mislabel(df):

    #we regard anomaly as positive and normal data as negative
    number_of_all_instances = len(df)
    TP = len(df[(df[label_column] == anomaly_value) & (df[ANOMALY] == if_anomaly_value)])
    FP = len(df[(df[label_column] == normal_value) & (df[ANOMALY] == if_anomaly_value)])
    TN = len(df[(df[label_column] == normal_value) & (df[ANOMALY] == if_normal_value)])
    FN = len(df[(df[label_column] == anomaly_value) & (df[ANOMALY] == if_normal_value)])

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1_score = 2 * precision * recall / (precision + recall)
    print(f'{number_of_all_instances} instances\nTP: {TP}\nFP: {FP}\nTN: {TN}\nFN: {FN}\nprecision: {precision}\nrecall: {recall}\nf1_score: {f1_score}\n')




if __name__ == '__main__':
    df = prepare_df(new_data_file_with_label, usePreprocessed=use_preprocessed)
    df = train_if(df)
    visualize(df)
    print_mislabel(df)
