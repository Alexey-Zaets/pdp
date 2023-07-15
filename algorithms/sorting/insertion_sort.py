from typing import Any

def insert(array: list, position: int, item: Any) -> None:
    i = position - 1
    while i >= 0 and array[i] > item:
        array[i+1] = array[i]
        i -= 1
    array[i+1] = item

def insertion_sort(array: list) -> None:
    # best case O(n)
    # average and worst case O(n**2)
    for i in range(len(array)):
        insert(array, i, array[i])
