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
    
#                               ----------------------------------------- Dejkstra algorithm -------------------------------------------------

# Imagine that we have simple weighted graph with two nodes A and B and weights 6 and 2. 
# Also graph has a finally node (fin variable).
graph = {}
# init a hash-table(dict) inside graph to collect weights and nodes names
graph['start'] = {}
# add weights
graph['start']['a'] = 6
graph['start']['b'] = 2
# let's include nodes and their neighbors
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
# the finaly node hasn't neighbors
graph['fin'] = {}

# Now we need to create dict for the costs(weights)
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity  # infinity is used because we don't know which node with its the weight we need to get to the final

# And we create dict for the parents
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# We don't need to process node more than once and we create a list of processed nodes
processed = []


# Write a function to find lowest cost node
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:  # loop over all nodes 
        cost = costs[node]
        if cost < lowest_cost and not in processed:  # if a node with the smallest cost and not processed
            lowest_cost = cost  # it wiil come new node with lowest cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)  # find a node with the lowest cost in not proceesed
while node is not None:  # None means that we have got to the finaly node
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # looping over all neighbors of node
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # if neigbour can be reached faster from this node
            costs[n] = new_cost  # refresh cost of this node
            parents[n] = node  # node comes a parent for his neighbour
    processed.append(node)  # node markes as processed
    node = find_lowest_cost_node(costs)  # repeat -->
