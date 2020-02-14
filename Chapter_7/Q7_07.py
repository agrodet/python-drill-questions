from multiprocessing import Process, Array


def add_all(fr, to, index, array):
    s = 0
    for n in range(fr, to + 1):
        s += n
    """①""" = s


worker = [None] * 10
result = """②"""
if __name__ == '__main__':
    for i in range(10):
        start = i * 10000
        end = (i + 1) * 10000 - 1
        worker[i] = Process(target=add_all, args="""③""")
        worker[i].start()
    s = 0
    for i in range(10):
        worker[i].join()
        s += """④"""
    print("{:,}".format(s))  # 4,999,950,000
