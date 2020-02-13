def transpose(mat):
    mat_t = [[0] * len(mat[0]) for i in range(len(mat))]
    for i, row in """①""":
        for j, elem in """②""":
            mat_t["""③"""]["""④"""] = elem
    return mat_t


result = transpose([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
print(result)
