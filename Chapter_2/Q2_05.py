def find_person(people, target):
    found = """①"""
    for i, person in enumerate("""②"""):
        if person == target:
            print(f"{target} is found at i == {"""③"""}.")
            found = """④"""
            break
    if not found:
        print(f"{"""⑤"""} is not here.")


find_person(['Wilma', 'Woof', 'Wally'], 'Wally')
find_person(['Wenda', 'Odlaw', 'WatcherA', 'WatcherB'], 'Whitebeard')
