def bubble_sort(array: list) -> None:
    # best case O(n)
    # average and worst case O(n**2)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
