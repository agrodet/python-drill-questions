from operator import itemgetter

fruits_quantity = {
    "イチゴ": 21,
    "ウメ": 51,
    "リンゴ": 14,
    "ナシ": 78,
    "バナナ": 2,
    "スイカ": 21
}

fruits_list = """①"""(fruits_quantity."""②""", key=itemgetter("""③"""), reverse="""④""")
for fruit, quantity in fruits_list:
    print(fruit + " → " + str(quantity))
    # 出力例：ナシ → 78
    #        ウメ → 51
    #        ...
