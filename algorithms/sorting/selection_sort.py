def selection_sort(array: list):
    # worst case, average case, best case O(n**2)
    for i in range(len(array)):
        lowest_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[lowest_idx]:
                lowest_idx = j
        array[i], array[lowest_idx] = array[lowest_idx], array[i]
