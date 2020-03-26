from threading import Thread, Barrier
from functools import reduce


def add_all(fr, to, index, barrier):
    s = 0
    for n in range(fr, to + 1):
        s += n
    result[index] = s
    """①"""


num = 10
result = [0] * num
th = [None] * num
b = Barrier("""②""")
for i in range(num):
    start = i * 10_000
    end = (i + 1) * 10_000 - 1
    th[i] = Thread(target=add_all, args="""③""")
    th[i].start()
"""④"""
print("{:,}".format(reduce(lambda x, y: x + y, result)))
# 出力結果 ＞＞＞ 4,999,950,000
