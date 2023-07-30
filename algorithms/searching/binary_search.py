def binary_search(items, value):
    items.sort()

    first = 0
    last = len(items)

    while first < last:
        mid = (first + last)//2
        if value <= items[mid]:
            last = mid
        else:
            first = mid + 1
    return -1 if first == len(items) or items[first] != value else first


def get_index(items, first, last, value):
    if first == last:
        return first

    mid = (first + last) // 2
    if value <= items[mid]:
        return get_index(items, first, mid, value)
    return get_index(items, mid + 1, last, value)


def recursion_binary_search(items, value):
    items.sort()

    first = get_index(items, 0, len(items), value)
    return -1 if first == len(items) or items[first] != value else first
