#!/usr/bin/env python
import os
import logging

DIR_APPDATA = os.getenv('APPDATA')
SPEEDTEST_CMD = 'C:\\Users\\LuisVillegas\\AppData\\Roaming\\Python\\Python38\\Scripts\\speedtest.exe'
LOG_FILE = 'speedtest.log'


def main():
    setup_logging()
    try:
        ping, download, upload = get_speedtest_results()
    except ValueError as err:
        logging.info(err)
    else:
        logging.info("%5.1f %5.1f %5.1f", ping, download, upload)
        # print(f"%5.1f %5.1f %5.1f", ping, download, upload)


def setup_logging():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M"
    )


def get_speedtest_results():
    """	Run test and parse results.
        Returns tuple of ping speed, download speed, and upload speed,
        or raises ValueError if unable to parse data."""
    ping = download = upload = None
    with os.popen(SPEEDTEST_CMD + ' --simple') as speedtest_output:
        for line in speedtest_output:
            label, value, unit = line.split()
            if 'Ping' in label:
                ping = float(value)
            elif 'Download' in label:
                download = float(value)
            elif 'Upload' in label:
                upload = float(value)

    if all((ping, download, upload)):
        return ping, download, upload
    else:
        raise ValueError('TEST FAILED')


if __name__ == '__main__':
    main()
