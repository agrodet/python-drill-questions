from multiprocessing import Process


def add_all(fr, to, index):
    s = 0
    for n in range(fr, to + 1):
        s += n
    result[index] = s


worker = [None] * 10
result = [0] * 10
if """①""":
    for i in range(10):
        start = i * 10_000
        end = (i + 1) * 10_000 - 1
        worker[i] = """②"""
        worker[i].start()
    s = 0
    for i in range(10):
        worker[i].join()
        print(result)
        s += result[i]
    print("{:,}".format(s))  # 出力結果 """③"""
