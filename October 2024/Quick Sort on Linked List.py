# User function Template for Python3

from collections import defaultdict  # Import defaultdict to fix the NameError

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)
        if not self.head:
            self.head = node
            return node
        tail.next = node
        return node

# Function to get the tail node of the linked list
def getTail(node):
    while node and node.next:
        node = node.next
    return node

# Function to partition the linked list around the pivot
def partition(start, end):
    if start == end:
        return start

    pivot_prev = start
    pivot = start
    curr = start.next

    while curr != end:
        if curr.data < pivot.data:
            pivot_prev = pivot_prev.next
            # Swapping data values
            pivot_prev.data, curr.data = curr.data, pivot_prev.data
        curr = curr.next

    # Swapping pivot data with pivot_prev to place pivot at the correct position
    pivot.data, pivot_prev.data = pivot_prev.data, pivot.data
    return pivot_prev

# Recursive quicksort function for linked list
def quickSortRec(start, end):
    if start != end and start != getTail(start):
        # Partition the list, and get the pivot node
        pivot = partition(start, end)
        # Recursively sort the left part
        quickSortRec(start, pivot)
        # Recursively sort the right part
        quickSortRec(pivot.next, end)

# Main quicksort function
def quickSort(head):
    quickSortRec(head, None)
    return head

# Helper function to print the linked list
def printList(head, dic):
    while head:
        if id(head) not in dic[head.data]:
            print("Don't swap data, swap pointer/node")
            return
        print(head.data, end=" ")
        head = head.next

# Testing function
def test_linked_list_sort():
    # Predefined test case
    test_cases = [
        [1, 6, 2],
        [1, 9, 3, 8],
        [10, 5, 1, 0, -1]
    ]
    
    for arr in test_cases:
        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        dic = defaultdict(list)  # Dictionary to keep data and id of node
        current = ll.head
        while current:
            dic[current.data].append(id(current))
            current = current.next

        resHead = quickSort(ll.head)
        printList(resHead, dic)  # Verifying and printing
        print()
        print("~")

# Run tests
test_linked_list_sort()
