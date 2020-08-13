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
  make_plot_file(df, plot_file_name)

def read_data():
  df = pd.io.parsers.read_csv(
    'speedtest.log',
    names='date time ping download upload'.split(),
    header=None,
    sep=r'\s+',
    parse_dates={'timestamp':[0,1]},
    na_values=['TEST','FAILED'],
  )
  print(df)
  return df[-48:]   # return data for last 48 periods (i.e., 24 hours)

def make_plot_file(last_24, file_plot_name):
  rcParams['xtick.labelsize'] = 'xx-small'

  plt.plot(last_24['timestamp'],last_24['download'], 'b-')
  plt.title('Casamar Apart. 66-b Bandwidth Report (last 24 hours)')
  plt.ylabel('Bandwidth in MBps')
  plt.yticks(range(0,20))
  plt.ylim(0.0,20.0)
  plt.xlabel('Date/Time')
  plt.xticks(rotation='45')
  plt.grid()
  
  current_axes = plt.gca()
  current_figure = plt.gcf()
  
  hfmt = dates.DateFormatter('%m/%d %H:%M')
  current_axes.xaxis.set_major_formatter(hfmt)
  current_figure.subplots_adjust(bottom=.25)
  
  loc = current_axes.xaxis.get_major_locator()
  loc.maxticks[dates.HOURLY] = [24]
  loc.maxticks[dates.MINUTELY] = [60]

  
  current_figure.savefig(file_plot_name)

if __name__ == '__main__':
  main()