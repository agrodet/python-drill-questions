import re


class PhoneReformatError(Exception):
    pass


def validate_phone_number(phone_number):
    pattern = "^"""①"""["""②"""](["""③"""]?[0-9]{"""④"""}){"""⑤"""}"
    if re.match(pattern, phone_number):
        return re."""⑥"""('"""③"""', '', phone_number)
    else:
        raise PhoneReformatError("Invalid phone number.")


print(validate_phone_number("0836656565"))
print(validate_phone_number("08 36 65 65 65"))
print(validate_phone_number("08.36.65.65.65"))
print(validate_phone_number("08-36-65-65-65"))
print(validate_phone_number("08|36|65|65|65"))
