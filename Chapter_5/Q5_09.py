import re


def check_balance(string):
    f_pattern = r"("""①"""?("""②""" " \
                    r"["""③"""]"""④""" \. ["""③"""]"""④""" " \
                    r"|" \
                    r"["""③"""]"""④"""))円"
    float_regex = re.compile(f_pattern, re.VERBOSE)
    balance = [float(s) for s in float_regex.findall(string)]
    return round(sum(balance), 2)
