def sum_rec(int_list, start):
    if start >= """①""":
        return 0
    return int_list[start] + sum_rec(int_list, """②""")


def to_binary_rec(num):
    if num == """③""":
        return ''
    return to_binary_rec("""④""") + str(num % 2)


print(sum_rec([2, 9, 11, 33], 0))
print(to_binary_rec(7))
print(to_binary_rec(11))
print(to_binary_rec(32))
