# Python program to test
# internet speed
import logging
import speedtest

SPEEDTEST = speedtest.Speedtest()
LOG_FILE = 'speedtest.log'


def main():
    setup_logging()
    try:
        ping, download, upload = get_speedtest_results()
    except ValueError as err:
        logging.info(err)
    else:
        logging.info("%5.1f %5.1f %5.1f", ping, download, upload)
        # print(ping, download, upload)


def setup_logging():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M",
    )


def get_speedtest_results():
    """	Run test and parse results.
            Returns tuple of ping speed, download speed, and upload speed,
            or raises ValueError if unable to parse data."""
    download = SPEEDTEST.download()
    download = round(download / (10 ** 6), 2)
    upload = SPEEDTEST.upload()
    upload = round(upload / (10 ** 6), 2)
    ping = SPEEDTEST.results.ping

    if all((ping, download, upload)):
        return ping, download, upload
    else:
        raise ValueError('TEST FAILED')


if __name__ == '__main__':
    main()
