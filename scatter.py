import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def scatter_plot(x, y):
    plt.figure(figsize=(12, 12))
    plt.scatter(x, y, s=200, alpha=0.8, c='darkgrey')
    plt.xlabel('x', fontsize=30)
    plt.ylabel('y', fontsize=30)
    plt.tick_params(labelsize=20)
    # plt.xlim([0, 100])
    # plt.ylim([0, 100])
    plt.tight_layout()
    plt.savefig('Scatter.jpeg')


def run():
    print('Enter input_name (xxx.xlsx or xxx.csv)')
    input_name = input()

    if 'xlsx' in input_name:
           df = pd.read_excel(input_name)
    elif 'csv' in input_name:
           df = pd.read_csv(input_name)
    else:
           raise ValueError('Invalid input name')

    x = df.iloc[:, 0]
    y = df.iloc[:, 1]

    scatter_plot(x, y)


if __name__ == '__main__':
        run()
