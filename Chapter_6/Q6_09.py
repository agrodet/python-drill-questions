import argparse

parser = argparse."""①"""(description="Calculate X to the power of Y")
parser."""②"""("x", type=int, help="the base")
parser."""②"""("y", type=int, help="the exponent")
args = parser."""③"""()

answer = """④""".x ** """④""".y

print("{}^{} = {}".format("""④""".x, """④""".y, """⑤"""))
