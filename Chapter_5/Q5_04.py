import re


def hexa_color_validation(hexa_color):
    hexa_pattern = r"^"""①"""(["""②"""]{"""③"""}"""④"""" \
                   r"["""②"""]{"""⑤"""})$"
    return re.search(hexa_pattern, hexa_color) is not None


# 関数のテスト
print(hexa_color_validation("#fff"))
print(hexa_color_validation("#fefefe"))
print(hexa_color_validation("#242424"))
print(hexa_color_validation("#24ff33"))
print(hexa_color_validation("#fof"))
print(hexa_color_validation("#24ff3o"))
print(hexa_color_validation("#ffff"))