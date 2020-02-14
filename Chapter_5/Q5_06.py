import re


def print_doubled_words(file_content):
    doubled = re.compile(r"\b"""①"""[ ("""②"""\b)+", re."""③""")

    for result in doubled.findall(file_content[0]):
        print(f"{result} on line {1}")

    for i in range(1, len(file_content)):
        for result in doubled.findall(file_content[i]):
            print(f"{result} on line {i + 1}")
        last_word = file_content[i - 1].split(' ')[-1]
        if last_word == file_content[i].split(' ')[0]:
            print(f"{last_word} repeated on lines {i} and {i + 1}"


test_string = ["The the story was not an happy one one.",
               "It started on a cold evening of winter in",
               "in a small town named Kongrad."]
print_doubled_words(test_string)