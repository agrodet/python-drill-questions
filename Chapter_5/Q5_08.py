import re


def password_validation(password):
    pattern = r"^("""①"""[^a-z]*["""②"""])" \
              r"("""①"""[^A-Z]*["""③"""])" \
              r"("""①"""\D*"""④""")" \
              r".{"""⑤"""}$"
    password_regex = re.compile(pattern)

    return password_regex.match(password) is not None
