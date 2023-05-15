import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_histgram(x):
    plt.figure(figsize=(15, 15))
    plt.hist(x, bins=15, color='darkgrey')
    plt.xlabel('Experimental selectivity (%)', fontsize=50, labelpad=10)
    plt.ylabel('Number', fontsize=50)
    plt.xlim(0, 100)
    plt.tick_params(labelsize=40)
    plt.tight_layout()
    plt.savefig('Histgram.jpeg')


def run():
    print('Enter input_name (xxx.xlsx or xxx.csv)')
    # input_name = input()
    input_name  = 'experimental_selectivity.xlsx'

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
