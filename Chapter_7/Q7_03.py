from threading import Thread
from functools import reduce


def add_all(fr, to, index):
    print(th[i].name)
    s = 0
    for n in range(fr, to + 1):
        s += n
    result[index] = s


result = [None] * 10
th = [None] * 10
for i in range(10):
    start = i * 10_000
    end = (i + 1) * 10_000 - 1
    args_d = """①"""
    th[i] = Thread(target=add_all, kwargs=args_d)
    th[i].start()
for i in range(10):
    th[i].join()
print(reduce(lambda x, y: x + y, result))  # 4999950000
