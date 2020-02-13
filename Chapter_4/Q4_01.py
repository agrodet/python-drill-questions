try:
    a = 100.0
    print(a[100])
except """1""" as ex:
    print(ex)  # 'float' object is not subscriptable

try:
    a = [100.0]
    print(a[-2])
except """2""" as ex:
    print(ex)  # list index out of range

try:
    a = 1
    print(a.propprop)
except """3""" as ex:
    print(ex)  # 'NoneType' object has no attribute 'propprop'

try:
    a = "Something Anything"
    print(a.len)
except """4""" as ex:
    print(ex)  # 'str' object has no attribute 'len'
