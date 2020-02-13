people = [["Alice", 16], ["Bob", 19], ["Carol", 18], ['Dan', 17], ['Erin', 20]]

name_list = list(map(lambda p: """①""", people))
print(name_list)

names_with_a = list(filter(lambda n: """②""", name_list))
print(names_with_a)

teenagers = list(filter(lambda p: """③""", people))
print(teenagers)

sum_of_ages = sum(map("""④""", people))
print(sum_of_ages)
