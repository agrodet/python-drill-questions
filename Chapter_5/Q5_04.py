import re


def hexa_color_validation(hexa_color):
    hexa_pattern = r"^"""①"""(["""②"""]{"""③"""}"""④"""" \
                   r"["""②"""]{"""⑤"""})$"
    return re.search(hexa_pattern, hexa_color) is not None
