directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]


def search_path_rec(map_array, visited, gx, gy, cx, cy):
    if (not 0 <= cy < len(map_array) or not 0 <= cx < len(map_array[cy])
            or visited[cy][cx] or """①""" == 0):
        return None
    """②"""[cy][cx] = True
    if cx == """③""" and cy == """④""":
        return [(cx, cy)]
    for direction in directions:
        path = search_path_rec(map_array, visited, gx, gy, """⑤""", """⑥""")
        if path is not None:
            path = [(cx, cy)] + """⑦"""
            break
    return path


def search_path(map_array):
    visited = [[False] * len(l) for l in map_array]
    path = search_path_rec(map_array, visited, len(map_array[0]) - 1, len(map_array) - 1, 0, 0)
    if path is None:
        print("No path found")
    else:
        print(f"A path found: {path}")


search_path([[1, 1, 1],
             [0, 1, 1],
             [1, 0, 1]])
search_path([[1, 0, 1, 0],
             [1, 0, 0, 0],
             [1, 0, 0, 1],
             [1, 1, 0, 1]])
search_path([[1, 0, 0, 1, 1],
             [1, 0, 0, 1, 0],
             [1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1],
             [0, 1, 0, 0, 1]])
