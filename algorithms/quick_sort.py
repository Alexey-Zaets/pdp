def quick_sort(array: list) -> list:
    # best case O(n * log2 n)
    # worst case O(n**2)
    if len(array) < 2:
        return array

    support_element = array[0]
    less = [i for i in array[1:] if i <= support_element]
    greater = [i for i in array[1:] if i > support_element]
    return quick_sort(less) + [support_element] + quick_sort(greater)
