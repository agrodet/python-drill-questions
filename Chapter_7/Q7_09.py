from multiprocessing import Process, Queue
from functools import reduce


def add_all(fr, to, index, queue):
    s = 0
    for n in range(fr, to + 1):
        s += n
    """①"""  # キューに追加する


worker = [None] * 10
result = [0] * 10
q = """②"""  # キューを用意する
if __name__ == '__main__':
    for i in range(10):
        start = i * 10_000
        end = (i + 1) * 10_000 - 1
        worker[i] = Process(target=add_all, args="""③""")
        worker[i].start()
    for i in range(10):
        worker[i].join()
        value = """④"""  # キューから値を取り出す
        result[value[0]] = value[1]
    print("{:,}".format(reduce(lambda x, y: x + y, result)))  # 4,999,950,000
