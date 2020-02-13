people = [("Alice", 16), ("Bob", 19), ("Carol", 18), ('Dan', 17), ('Erin', 20)]


def get_name(person):
    return person[0]


def get_age(person):
    return person[1]


def name_contains_a(name):
    return 'a' in name


def is_teenager(person):
    return 12 < get_age(person) < 20


name_list = list(map("""①""", people))  # blank
print(name_list)

names_with_a = list(filter("""②""", name_list))  # blank
print(names_with_a)

teenagers = list("""③"""("""④""", people))  # blank
print(teenagers)

sum_of_ages = sum("""⑤"""("""⑥""", people))  # blank
print(sum_of_ages)
