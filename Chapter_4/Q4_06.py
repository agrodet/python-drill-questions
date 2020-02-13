try:
    a = [1, 2, 3, 4, 5]
    s = 0
    for ix in range(6):
        s += a[-ix]
except Exception as ex:
    print(ex)
print(f"ix={ix}, s={s}")
