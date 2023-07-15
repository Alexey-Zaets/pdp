def is_equal(first, second):
    return first == second


def is_not_more(first, second):
    return first <= second


def merge(left_part: list, right_part: list) -> list:
    sorted_list = []
    left_index = right_index = 0
    left_length, right_length = len(left_part), len(right_part)

    for _ in range(left_length + right_length):
        if left_index < left_length and right_index < right_length:
            if is_not_more(left_part[left_index], right_part[right_index]):
                sorted_list.append(left_part[left_index])
                left_index += 1
            else:
                sorted_list.append(right_part[right_index])
                right_index += 1

        elif is_equal(left_index, left_length):
            sorted_list.append(right_part[right_index])
            right_index += 1

        elif is_equal(right_index, right_length):
            sorted_list.append(left_part[left_index])
            left_index += 1

    return sorted_list

def merge_sort(array: list) -> list:
    # best, average and worst case O(n * log2 n)
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left_part = merge_sort(array[:mid])
    right_part = merge_sort(array[mid:])
    return merge(left_part, right_part)
