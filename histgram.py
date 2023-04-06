import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_histgram(x):
    plt.figure(figsize=(12, 12))
    plt.hist(x, bins=10, color='darkgrey')
    plt.xlabel('x', fontsize=30)
    plt.ylabel('Number', fontsize=30)
    plt.tick_params(labelsize=30)
    plt.tight_layout()
    plt.savefig('Histgram.jpeg')


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

    plot_histgram(x)


if __name__ == '__main__':
    run()