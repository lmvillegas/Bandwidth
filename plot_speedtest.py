import os
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import dates, rcParams


HOSTNAME = os.getenv('COMPUTERNAME')
TITLE = 'Ancho de Banda de ' + f'{HOSTNAME}'
YLABEL = 'Ancho de Banda en MBps'
XLABEL = "Ultimas 24 Horas"
xrange = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
LOG_FILE = (f'speedtest-{HOSTNAME}.log')


def main():
    plot_file_name = 'bandwidth.png'
    create_plot(plot_file_name)
    os.system('open ' + plot_file_name)


def create_plot(plot_file_name):
    df = read_data()
    make_plot_file_last_24(df, plot_file_name)


def read_data():
    df = pd.io.parsers.read_csv(
        LOG_FILE,
        names='date time ping download upload'.split(),
        header=None,
        sep=r'\s+',
        parse_dates={'timestamp': [0, 1]},
        na_values=['TEST', 'FAILED'],
    )

    # print(df)
    return df[-48:]


def make_plot_file_last_24(last_24, file_plot_name):
    rcParams['xtick.labelsize'] = 'xx-small'
    plt.plot(last_24['timestamp'], last_24['download'], 'b-')
    plt.title(f'{TITLE}')
    plt.ylabel(f'{YLABEL}')
    plt.yticks(xrange)
    plt.ylim(0.0, 10.0)
    plt.xlabel(f'{XLABEL}')
    plt.xticks(rotation='45')
    plt.grid()
    # plt.show()

    current_axes = plt.gca()
    current_figure = plt.gcf()

    hfmt = dates.DateFormatter('%m/%d %H:%M')
    current_axes.xaxis.set_major_formatter(hfmt)
    current_figure.subplots_adjust(bottom = .25)

    loc = current_axes.xaxis.get_major_locator()
    loc.maxticks[dates.HOURLY] = 24
    loc.maxticks[dates.MINUTELY] = 60

    current_figure.savefig(file_plot_name)


if __name__ == '__main__':
    main()
