def find_person(people, target):
    for i, person in enumerate(people):
        if person == target:
            print(f"{target} is found at i == {i}.")
            """①"""
    """②""":
        print(f"{target} is not here.")


find_person(['Wilma', 'Woof', 'Wally'], 'Wally')
find_person(['Wenda', 'Odlaw', 'WatcherA', 'WatcherB'], 'Wally')
