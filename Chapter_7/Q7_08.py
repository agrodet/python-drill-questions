from multiprocessing.pool import Pool


def add_all(fr, to, index):
    s = 0
    for n in range(fr, to + 1):
        s += n
    """①"""


    worker = [None] * 10
    if __name__ == '__main__':
        with """②""" as pool:
            for i in range(10):
                start = i * 10_000
                end = (i + 1) * 10_000 - 1
                worker[i] = """③"""
            s = 0
            for i in range(10):
                s += worker[i]."""④"""
            print("{:,}".format(s))  # 4,999,950,000
