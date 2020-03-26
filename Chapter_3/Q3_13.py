from operator import itemgetter

fruits_quantity = {
    "イチゴ": 21,
    "ウメ": 51,
    "リンゴ": 14,
    "ナシ": 78,
    "バナナ": 2,
    "スイカ": 21
}

fruits_sorted = """①"""(fruits_quantity."""②""",
                         key=itemgetter("""③"""),
                         reverse="""④""")
for fruit, quantity in fruits_sorted:
    print(fruit + " → " + str(quantity))
    # 出力結果  ナシ → 78
    #          ウメ → 51
    #          イチゴ → 21
    #          スイカ → 21
    #          リンゴ → 14
    #          バナナ → 2
