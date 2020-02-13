class Counter:
    created = 0

    def __init__(self):
        Counter.created += 1

    @classmethod
    def how_many(cls):
        return cls.created


a = Counter()
b = Counter()
del a
c = Counter()
del b
print(Counter.how_many())  # ここで、"""①"""と出力される
