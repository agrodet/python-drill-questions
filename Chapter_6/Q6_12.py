import signal
import sys
from datetime import datetime


def log_time(signal, frame):
    """Function called when the program closes"""
    with open("log.txt", "a") as f:
        f.write("Script interrupted - {} \n".format(datetime.now()))
    """①"""(0)


signal."""②"""(signal.SIGINT, """③""")

while True:
    continue
