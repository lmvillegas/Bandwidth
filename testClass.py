import os
import plot_speedtest

HOSTNAME = os.getenv('COMPUTERNAME')
LOG_FILE = (f'speedtest-{HOSTNAME}.log')
print (LOG_FILE)