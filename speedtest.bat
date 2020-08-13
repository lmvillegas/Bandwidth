SET logfile="c:\Bandwidth\batch.log"
@echo off
@echo Starting Script at %date% %time% >> %logfile%
PUSHD  "c:\Bandwidth\"
python  log_speedtest.py  %*
@echo finished at %date% %time% >> %logfile%
