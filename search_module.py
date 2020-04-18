import time


def binary_search(list_in: list, item: int) -> int:
    """
    If item exists in list_in, this function returns its position in the list.
    """

    list_in.sort()

    low = 0
    high = len(list_in) - 1
    found = False
    count = 0
    t1 = time.perf_counter()

    try:
        while(low <= high and not found):
            mid = (low + high) // 2
            count += 1
            if list_in[mid] == item:
                found = True
            else:
                if item < list_in[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        print(list_in.index(item))

    except ValueError:
        print(f"{item} is not in list")

    t2 = time.perf_counter()
    print(f"binary search: {item} found")
    print(f"in {t2-t1} seconds")
    print(f"and in {count} halvings")



def find(list_in: list, item: int) -> int:
    t1 = time.perf_counter()

    if item in list_in:
        print(list_in.index(item))
    else:
        print(f"{item} is not in list")

    t2 = time.perf_counter()
    print(f"find took {t2-t1} seconds")


#binary_search([0, 1, 2, 3, 12, 5, 6, 7, 8, 9, 10, 11], 12)
#binary_search([3,6,7,1,5,8,9,11,12,15,13,14,16,17,19,2,4,10,18,20], 5)


test_list = [i for i in range(10000000)]
n = 1919
binary_search(test_list, n)
find(test_list, n)


#binary_search([0, 1, 2, 3, 12, 5, 6, 7, 8, 9, 10, 11], 12)
#binary_search([3,6,7,1,5,8,9,11,12,15,13,14,16,17,19,2,4,10,18,20], 25)

# test_list = [i for i in range(1000)]
# binary_search(test_list, 999)
# find(test_list, 999)