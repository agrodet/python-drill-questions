import re


def count_dogs(text):
    inu_pattern = r"("""①""""""②"""|"""③"""|"""④""")犬"
    return len(re.findall(inu_pattern, text))
