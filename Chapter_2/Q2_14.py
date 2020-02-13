def trace_call(f):
    def traced(*args, **kwargs):
        args_str = ', '.join(map(str, args))
        print(f"start of {f.__name__}({args_str})")
        result = f(*args, **kwargs)
        print(f"end of {f.__name__}({args_str})")
        return """①"""
    return """②"""


@"""③"""
def ackerman(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackerman(m - 1, 1)
    else:
        return ackerman(m - 1, ackerman(m, n - 1))


print(ackerman(2, 0))
