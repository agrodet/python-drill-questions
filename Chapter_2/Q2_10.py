import datetime
import time


def sleep_3s():
    print('I am sleepy...')
    time.sleep(3)
    return "I had a good sleep!"


def measure_time(func):
    print(f""""①""" at: {datetime.datetime.now()}")
    result = """②"""
    print(f""""③""" at: {datetime.datetime.now()}")
    return """④"""


print(measure_time(sleep_3s))
