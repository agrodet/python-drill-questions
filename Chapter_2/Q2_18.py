def parse_rec(text, current_depth):
    index = 0
    result_texts = []
    current_text = ""
    while (index < len(text)):
        if text[index] == "(":
            each_index, each_result = parse_rec(text"""①""", """②""")
            if each_index is """③""":
                return None, []
            index += each_index + """④"""
            result_texts += each_result
        elif text[index] == ")":
            if current_depth """⑤""" 0:
                return None, []
            break
        else:
            current_text += text[index]
            index += 1
    else:
        if current_depth """⑥""" 0:
            return None, []

    if len(current_text) > 0:
        result_texts += [f"{c}: {current_depth}" for c in """⑦"""]
    return index, result_texts


def parse(text):
    (read_pos, results) = parse_rec(text, 0)
    if (read_pos is None):
        print("unbalanced")
    else:
        print(', '.join(results))


parse("((A))")  # A: 2
parse("(()))")  # unbalanced
parse("(((B)((C))))T")  # B: 3, C: 4, T: 0
parse("(((D))(G((E))H)(F))")  # D: 3, E: 4, G:2, H: 2, F: 2
parse("((((I)(J)))")  # unbalanced
