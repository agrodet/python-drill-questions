def format_float(number):
    if type(number) is not float:
        raise TypeError("引数のタイプはfloatではありません")
    number = str(number)
    integer_part, float_part = number."""①"""(".")
    return ","."""②"""([integer_part, float_part["""③"""]])


print(format_float(3.999999999))  # 出力結果 ＞＞＞ 3,999
print(format_float(1.5))  # 出力結果 ＞＞＞ 1,5
