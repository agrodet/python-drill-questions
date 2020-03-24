import re


def check_balance(string):
    float_pattern = r"("""①"""?("""②""" " \
                    r"["""③"""]"""④""" \. ["""③"""]"""④""" " \
                    r"|" \
                    r"["""③"""]"""④"""))円"
    float_regex = re.compile(float_pattern, re.VERBOSE)
    print(float_regex.findall(string))
    balance = [float(s) for s in float_regex.findall(string)]
    return round(sum(balance), 2)
