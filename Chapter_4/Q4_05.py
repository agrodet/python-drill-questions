try:
    a = [1, 2, 3, 4, 5]
    s = 0
    for ix in range(10):
        s += a[ix]
except """1""" as ex:
    print(ex)
print(f"ix={ix}, s={s}")
# 出力結果
# list index out of range
# ix="""②""", s="""③"""