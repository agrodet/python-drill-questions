import re

kit_pattern = "kit*"

input_strings = ["kit",
                 "kat",
                 "kitty",
                 "katty",
                 "kittkatt",
                 "toolkit",
                 "kiwi",
                 ""]

match = []
for m in map(lambda s: re.search(kit_pattern, s), input_strings):
    match.append(m.group(0)) if m is not None else match.append("None")
print(match)
# 出力結果
# [""""①"""",
# """"②"""",
# """"③"""",
# """"④"""",
# """"⑤"""",
# """"⑥"""",
# """"⑦"""",
# """"⑧""""]
