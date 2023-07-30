def bubble_sort(items: list) -> list:
    # best case O(n)
    # average and worst case O(n**2)
    for _ in range(len(items) - 1, 0, -1):
        for i in range(len(items) - 1):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
    return items
