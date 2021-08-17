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

#                               ----------------------------------------- SELECTION SORT ---------------------------------------------
# For the first time we need to find out a index of a smallest value in the array
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
# Sort function
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))  # At this point we need to get smallest value and delete it from original array,
    return newArr                         # it's why we using pop() method here!

#                               ----------------------------------------- QUICK SORT -------------------------------------------------
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]  # Опорный элемент
        
        '''Опорный элемент массива, выбирается случайным или посередине массива т.к. в этом случае
        время выполнения составит O(n * log(n)) , а если брать первый элемент массива то это будет O(n^2)'''
        
        less = [_ for _ in array[1:] if _ < pivot]  # Сортировка элементов меньших опорного
        greater = [_ for _ in array[1:] if _ > pivot]  # Сортировка элементов больше опорного
        return quicksort(less) + [pivot] + quicksort(greater)  # Применяем рекурсивный вызов функции!
