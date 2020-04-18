

def binary_search(list_in: List[int], item: int) -> int:
    """
    If item exists in list_in, this function returns its position in the list.
    """

    list_in.sort()

    low = 0
    high = len(list_in) - 1
    found = False
    while(low <= high and not found):
        mid = (low + high) // 2
        if list_in[mid] == item:
            found = True
        else:
            if item < list_in[mid]:
                high = mid - 1
        else:
            low = mid + 1
    print(list_in.index(item))


i want to sort the list form low to high,
then use the binary search method,
to half the list and search again.
once found, return index
