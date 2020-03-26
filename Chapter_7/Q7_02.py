from threading import Thread, Lock


def add_value(value):
    """①""" cumulative
    lock."""②"""  # 計算が正しくなるように追加した
    cumulative += value
    """③"""  # 計算が正しくなるように追加した

def add_all(fr, to):
    for n in range(fr, to + 1):
        add_value(n)

cumulative = 0
lock = """④"""  # 計算が正しくなるように追加した
th = [None] * 10
for i in range(10):
    start = i * 1_000_000
    end = (i + 1) * 1_000_000 - 1
    th[i] = Thread(target=add_all, args=(start, end))
    th[i].start()
for i in range(10):
    th[i].join()
print("{:,}".format(cumulative))  # 修正前の出力例 18,729,807,728,754
