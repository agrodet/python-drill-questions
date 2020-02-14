from threading import Thread, Lock


def add_value(value):
    global cumulative
    if """①""":
        """②""" Exception('競合が発生しました')
    cumulative += value
    lock.release()


def add_all(fr, to):
    for n in range(fr, to + 1):
        add_value(n)


cumulative = 0
lock = Lock()
th = [None] * 10
for i in range(10):
    start = i * 1000000
    end = (i + 1) * 1000000 - 1
    th[i] = Thread(target=add_all, args=(start, end), name=f"th{i}")
    th[i].start()
for i in range(10):
    th[i].join()
print(cumulative)  # 18729807728754
# Check
s = 0
for i in range(10000000):
    s += i
print(s)  # 49999995000000
