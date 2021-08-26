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
import random

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array)  # Опорный элемент
        
        '''Опорный элемент массива, выбирается случайным или посередине массива т.к. в этом случае
        время выполнения составит O(n * log(n)) , а если брать первый элемент массива то это будет O(n^2)'''
        
        less = [i for i in array if i < pivot]  # Сортировка элементов меньших опорного
        greater = [i for i in array if i > pivot]  # Сортировка элементов больше опорного
        return quicksort(less) + [pivot] + quicksort(greater)  # Применяем рекурсивный вызов функции!
   
#                               ----------------------------------------- BREADTH FIRST SEARCH -------------------------------------------------

from collections import deque


def some_condition():  # function that we want to perform with our graph
    pass  # should return True or False


graph = {}  # creates a graph
"""
Our graph looks like:
{I'm : [friend_1, friend_2, friend_3]
friend_1 : [friend_of_friend_1]
friend_2 : [friend_of_friend_2]
...}
"""


def breadth_first_search(name):
    search_queue = deque()  # creates deque to collect names in queue
    search_queue += graph[name]
    searched = []  # list of elements that have been searched
    while search_queue:
        deque_element = search_queue.popleft()  # takes left element from queue
        if deque_element not in searched:
            if some_condition():
                print(deque_element)
                return True
            else:
                search_queue += graph[deque_element]  # appends the next level elements to queue
                searched.append(deque_element)  # appends element to searched list
        return False
    
