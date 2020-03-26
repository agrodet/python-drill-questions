def arbitrary(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


arbitrary(1, 2, 3, 4)
arbitrary(1, 2, a=3, b=4)

# 出力結果
# args: """①"""
# kwargs: {}
# args: """②"""
# kwargs: {"""③""": 3, """④""": 4}
