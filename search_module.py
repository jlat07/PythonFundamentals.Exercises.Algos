

def binary_search(list_in: list, item: int) -> int:
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


binary_search([0, 1, 2, 3, 12, 5, 6, 7, 8, 9, 10, 11], 12)
binary_search([3,6,7,1,5,8,9,11,12,15,13,14,16,17,19,2,4,10,18,20], 5)
