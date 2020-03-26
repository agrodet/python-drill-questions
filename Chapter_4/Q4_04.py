s = """1"""
k = 10
z = 0
try:
    print(s / k)
except ZeroDivisionError:
    print("0で割らないでね")
except TypeError:
    print("計算は文字列でなく、数値を与えてね")
    print("おそらく計算結果は{}".format(int(s) / int(k)))
except Exception as ex:
    print(f"Type={type(ex)}, {ex}")
# 出力結果
# 計算は文字列でなく、数値を与えてね
# おそらく計算結果は9.8
