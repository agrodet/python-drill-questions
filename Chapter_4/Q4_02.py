# このコードは、"""①"""のエラーが検出され
a = {"shirt": 7, "pants": 2, "socks": 8}
print(sum(a))

# このコードは、"""②"""のエラーが検出され
a = set([x * x for x in range(0, 5)])
a.remove(7)

# このコードは、"""③"""のエラーが検出され
example = [x for x in range(0, 10)]
for i in range(0, len(example)):
    if example[i] % 2 == 0:
        example.remove(example[i])

# このコードは、"""④"""のエラーが検出され
a = (1, 2, 3)
b = (0, 2, 5)
for i in range(0, len(a)):
    if a[i] == b[i]:
        b[i] = a[i]
