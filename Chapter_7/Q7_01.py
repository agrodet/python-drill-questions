from """①""" import Thread
from functools import reduce


def add_all(fr, to, index):
    s = 0
    for n in range(fr, to + 1):
        s += n
    result[index] = s


result = [0] * 10
th = [None] * 10
for i in range(10):
    start = """②"""
    end = """③"""
    th[i] = Thread(target="""④""", args=(start, end, i))
    th[i].start()
for i in range(10):
    th[i]."""⑤"""
print("{:,}".format(reduce(lambda x, y: x + y, result)))  # 出力例＞＞＞ 4,999,950,000
