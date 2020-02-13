def arbitrary(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


arbitrary(1, 2, 3, 4)
arbitrary(1, 2, a=3, b=4)
