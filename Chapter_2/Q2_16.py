def dropped_list(src_list, i):
    return [x for k, x in enumerate(src_list) if k != i]


def all_permutations(num_list):
    if num_list == []:
        return """①"""
    result_list = []
    for i, elem in enumerate(num_list):
        result_list """②""" list(map(lambda perm: """③""" + perm,
                                all_permutations("""④""")))
    return result_list


print(all_permutations([1, 2, 3]))
