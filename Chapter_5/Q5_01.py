import re


def jp_postal_code_validation(postal_code):
    return re.search(r""""①"""{"""②"""}-"""①"""{"""③"""}",
                     postal_code) is not None
