def min_edit_distance(first: str, second: str) -> int:
    first_len, second_len = len(first), len(second)

    result = [
        [0 for _ in range(second_len + 1)]
        for _ in range(first_len + 1)
    ]

    for i in range(1, first_len + 1):
        result[i][0] = i

    for j in range(1, second_len + 1):
        result[0][j] = j

    for i in range(1, first_len + 1):
        for j in range(1, second_len + 1):

            cost = 1
            if first[i-1] == second[j-1]:
                cost = 0

            replaced_cost = result[i-1][j-1] + cost
            removed_cost = result[i-1][j] + 1
            inserted_cost = result[i][j-1] + 1
            result[i][j] = min(replaced_cost, removed_cost, inserted_cost)

    return result[first_len][second_len]

