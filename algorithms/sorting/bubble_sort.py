def bubble_sort(items: list) -> None:
    # best case O(n)
    # average and worst case O(n**2)
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            items[i], items[i + 1] = items[i + 1], items[i]
