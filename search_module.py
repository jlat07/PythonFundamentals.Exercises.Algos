import time


def binary_search(list_in: list, item: int) -> int:
    """
    If item exists in list_in, this function returns its position in the list.
    :param list_in: list of sorted integers
    :return: Index of item in list_in
    """

    low = 0
    high = len(list_in) - 1
    count = 0
    t1 = time.perf_counter()
    while low <= high:
        count += 1
        middle = (low + high)//2
       
        if list_in[middle] == item:
            break
        elif list_in[middle] > item:
            high = middle - 1
        else:
            low = middle + 1
    t2 = time.perf_counter()
    return list_in.index(item)
    print(f"binary search: {item} found at index {list_in.index(item)}")
    print(f"elapsed time: {t2-t1} seconds")
    print(f"halvings: {count} ")


def find(list_in: list, item: int) -> int:
    """
    If item exists in list_in, this function returns its position in the list.
    :param list_in: list of integers
    :return: Index of item in list_in
    """
    t1 = time.perf_counter()

    if item in list_in:
        print(f"linear search: {item} found at index {list_in.index(item)}")
    else:
        print(f"{item} is not in list")

    t2 = time.perf_counter()
    print(f"elapsed time: {t2-t1} seconds")
