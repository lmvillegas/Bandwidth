#!/usr/bin/env python

import os
import matplotlib.pyplot as plt
from matplotlib import dates, rcParams
import pandas as pd


def main():
    plot_file_name = 'bandwidth.png'
    create_plot(plot_file_name)
    os.system('open ' + plot_file_name)


def create_plot(plot_file_name):
    df = read_data()
    make_plot_file_last_24(df, plot_file_name)


def read_data():
    df = pd.io.parsers.read_csv(
        'speedtest.log',
        names='date time ping download upload'.split(),
        header=None,
        sep=r'\s+',
        parse_dates={'timestamp': [0, 1]},
        na_values=['TEST', 'FAILED'],
    )
    print(df)
    return df[-48:]  # return data for last 48 periods (i.e., 24 hours)


def make_plot_file_last_24(last_24, file_plot_name):
    rcParams['xtick.labelsize'] = 'xx-small'

    plt.plot(last_24['timestamp'], last_24['download'], 'b-')
    plt.title('Ancho de Banda de Casamar Apart 66-B')
    plt.ylabel('Ancho de Banda en MBps')
    xrange = (0, 1, 2, 3, 4, 5)
    plt.yticks(xrange)
    plt.ylim(0.0, 5.0)
    plt.xlabel('Fecha/Hora')
    plt.xticks(rotation='90')
    plt.grid()

    current_axes = plt.gca()
    current_figure = plt.gcf()

    # hfmt = dates.DateFormatter('%m-%d %H:%M')
    # current_axes.xaxis.set_major_formatter(hfmt)
    # current_figure.subplots_adjust(bottom=.35)

    current_axes.xaxis.set_major_locator(dates.DayLocator(interval=1))
    current_axes.xaxis.set_major_formatter(dates.DateFormatter('%d-%m %H:%M'))
    # locator = dates.MinuteLocator(interval=30)
    # locator.MAXTICKS = 5000
    # current_axes.xaxis.set_minor_locator(locator)

    # datemin = pd.datetime()
    # current_axes.set_xlim(datemin)

    current_figure.savefig(file_plot_name)


if __name__ == '__main__':
    main()
