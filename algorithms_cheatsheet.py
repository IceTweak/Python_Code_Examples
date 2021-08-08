#                               ----------------------------------------- BINARY SEARCH ---------------------------------------------
def binary_search (lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = mid + 1
        if guess < item:
            low = mid + 1
        elif guess == item:
            return mid
        else:
             high = mid - 1
    return None